from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'category'

    def __str__(self):
        return self.name
