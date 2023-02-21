from rest_framework.serializers import ModelSerializer

from main_app.models import *


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
