from django.contrib import admin

from .models import *


class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price')

    list_display = ('id', 'name', 'description', 'price')

    list_display_links = ('id', 'name')

    search_fields = ('name', 'description')

    list_filter = ('price',)


class OrderItemAdmin(admin.ModelAdmin):
    fields = ('ordered', 'item', 'quantity')

    list_display = ('id', 'ordered', 'item', 'quantity')

    list_display_links = ('id',)


class OrderAdmin(admin.ModelAdmin):
    fields = ('items', 'ordered_date', 'ordered')

    list_display = ('id', 'ordered_date', 'ordered')

    list_display_links = ('id', )

    search_fields = ('id',)

    list_filter = ('ordered_date', 'ordered')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
