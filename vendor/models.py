from django.db import models


class Restaurant(models.Model):
    restaurant_id = models.CharField(max_length=50, primary_key=True)
    restaurant_name = models.CharField(max_length=100)

    def __str__(self):
        return self.restaurant_name + ' ' + self.restaurant_id
