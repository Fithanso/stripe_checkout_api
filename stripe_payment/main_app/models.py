from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.CharField(max_length=255, verbose_name='Description')
    # Prices are stored in cents
    price = models.IntegerField(verbose_name='Price')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"
        ordering = ["name"]


class OrderItem(models.Model):
    ordered = models.BooleanField(default=False, verbose_name='Ordered')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Item')
    quantity = models.IntegerField(default=1, verbose_name='Quantity')
    order = models.ForeignKey('Order', default=None, on_delete=models.CASCADE, related_name='order_items',
                              verbose_name='Order')

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    class Meta:
        verbose_name = "order item"
        verbose_name_plural = "order items"


class Order(models.Model):

    ordered_date = models.DateTimeField(null=True, verbose_name='Date of ordering')
    ordered = models.BooleanField(default=False, verbose_name='Ordered')

    def __str__(self):
        return 'Order ' + str(self.pk)

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"
