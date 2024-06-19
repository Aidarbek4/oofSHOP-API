from django.db import models
from user.models import User


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        db_table = 'review'

    def __str__(self):
        return f'Отзыв от {self.user.name}'
