from django.http import HttpResponseRedirect
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

from .classes import StripeManager
from .models import Item
from stripe_payment import settings


class BuyItem(APIView):

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)

        sm = StripeManager()
        item_price = int(item.price)

        session = sm.create_checkout_session(item.name, item_price)
        print(session.url)

        response_body = {'session_id': session.id}

        return Response(response_body)


class ItemCheckout(APIView):
    renderer_classes = (TemplateHTMLRenderer,)

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        return Response({'item': item, 'stripe_publishable_api_key': settings.STRIPE_PUBLISHABLE_API_KEY},
                        template_name='main_app/checkout.html')
