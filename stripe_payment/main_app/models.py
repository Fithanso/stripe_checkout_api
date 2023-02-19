from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    # Prices are stored in cents
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"
        ordering = ["name"]
