from django.urls import re_path
from .views import *

urlpatterns = [
    re_path("buy/(?P<pk>\d+)/$", BuyItem.as_view(), name="buy_item"),
    re_path("item/(?P<pk>\d+)/$", ItemCheckout.as_view(), name="item_checkout")
]
