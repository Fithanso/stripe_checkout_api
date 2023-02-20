from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .classes import StripeManager
from .models import *
from .serializers import *
from .functions import *
from .validators import *
from stripe_payment import settings


class BuyItems(APIView):
    # post is more comfortable when we need to pass multiple ids
    permission_classes = [AllowAny]

    def get(self, request):
        if not validate_passed_item_ids(request.GET.get("item_ids")):
            raise APIException(detail="Please provide correct order items' ids", code=400)

        order_items = get_order_items_from_ids(request.GET.get('item_ids'))

        sm = StripeManager()
        session = sm.create_checkout_session(order_items)

        response_body = {'session_id': session.id}

        return Response(response_body)


class ItemCheckout(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):

        if not validate_passed_item_ids(request.GET.get('item_ids')):
            return Response({"error": "Please provide correct order items' ids"},
                            template_name='main_app/checkout.html')

        order_items = get_order_items_from_ids(request.GET.get('item_ids'))

        if not order_items:
            return Response({"error": "Provided order items' ids do not exist"},
                            template_name='main_app/checkout.html')

        context_data = {
            'items': order_items,
            'stripe_publishable_api_key': settings.STRIPE_PUBLISHABLE_API_KEY,
            'buy_request_link': reverse('buy_item') + '?item_ids=' + request.GET.get('item_ids')
        }

        return Response(context_data, template_name='main_app/checkout.html')


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    permission_classes = [AllowAny]


class OrderItemViewSet(ModelViewSet):
    serializer_class = OrderItemSerializer

    permission_classes = [AllowAny]

    def get_queryset(self):
        # to filter with get parameters item&order
        queryset = OrderItem.objects.all()
        # to get OrderItems that contain the item
        item_id = self.request.query_params.get('item')
        if item_id is not None:
            get_object_or_404(OrderItem, pk=item_id)
            queryset = queryset.filter(item=item_id)

        # to get OrderItems that belong to the order
        order_id = self.request.query_params.get('order')
        if order_id is not None:
            get_object_or_404(Order, pk=order_id)
            queryset = queryset.filter(order=order_id)

        return queryset
