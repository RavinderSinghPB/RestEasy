from rest_framework import serializers, request
from users.models import User
from dish.models import Dish, DishDetails
from orders.models import Order, OrderItem
from vendor.models import Restaurant


class UserSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'vendor')
        extra_kwargs = {'password': {'write_only': True, }}


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('url', 'restaurant_id', 'restaurant_name',)


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ('url', 'name', 'calorie')


class DishDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DishDetails
        fields = ('url', 'dish', 'restaurant', 'price', 'speciality',)


class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('url', 'item', 'quantity', 'status')


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Order
        fields = ('url','items', 'date_time',)
