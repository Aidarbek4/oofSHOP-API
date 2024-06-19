from django.db import models
from product.models import Product
from user.models import User


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    quantity = models.IntegerField()
    price = models.FloatField()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        db_table = 'order'

    def __str__(self):
        return f'Заказ от {self.owner.name}'
