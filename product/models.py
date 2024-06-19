from django.db import models

from django.db import models

from category.models import Category


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.FloatField()
    image = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        db_table = 'product'

    def __str__(self):
        return f'Товар {self.title}'
