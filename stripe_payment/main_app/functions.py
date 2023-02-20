from rest_framework.generics import get_object_or_404

from main_app.models import OrderItem


def get_order_items_from_ids(ids_str):
    order_item_ids = ids_str.split(",")
    order_items = OrderItem.objects.filter(pk__in=order_item_ids).select_related('item')

    return order_items
