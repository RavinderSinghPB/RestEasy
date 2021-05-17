from django.db import models
from vendor.models import Restaurant

'''
11. Each Dish should contain Name, calories fields
12. A Dish can be sold by different vendor with different price. Only the name and calories will be
same across the vendors.
'''


class Dish(models.Model):
    name = models.CharField(max_length=200)
    calorie = models.FloatField()

    def __str__(self):
        return self.name


class DishDetails(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=3)
    speciality = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.dish) + ' ' + str(self.restaurant) + ' ' + str(self.price)
