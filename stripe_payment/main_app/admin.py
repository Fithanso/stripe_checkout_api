from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'price')

    list_display = ('id', 'name', 'description', 'price')

    list_display_links = ('id', 'name')

    search_fields = ('name', 'description')

    list_filter = ('price',)


admin.site.register(Item, ItemAdmin)
