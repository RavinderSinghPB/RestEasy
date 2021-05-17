from django.db import models

from dish.models import DishDetails
from users.models import User


class OrderItem(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    item = models.ForeignKey(DishDetails, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    Status_choices = (
        ('c', 'In Cart'),
        ('o', 'Ordered')
    )

    status = models.CharField(max_length=1, choices=Status_choices, default='c')

    def __str__(self):
        return str(self.item) + str(self.quantity)


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    items = models.ManyToManyField(OrderItem)

    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer)
