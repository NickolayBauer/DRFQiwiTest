from django.db import models


class Order(models.Model):
    description = models.TextField(max_length=200, verbose_name='Описание заказа')
    cost = models.PositiveIntegerField(verbose_name="Стоимость")

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.cost + "$"
