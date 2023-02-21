from django.urls import re_path
from rest_framework.routers import SimpleRouter


from .views import *

router = SimpleRouter()
router.register(r'items', ItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet, basename='order-item')

urlpatterns = [
    re_path("buy/", BuyItems.as_view(), name="buy_item"),
    re_path("item/", ItemCheckout.as_view(), name="item_checkout")
]

urlpatterns += router.urls

