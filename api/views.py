from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from dish.models import Dish, DishDetails
from orders.models import Order, OrderItem
from users.models import User
from vendor.models import Restaurant
from .serializers import UserSerializer, DishSerializer, DishDetailsSerializer, OrderItemSerializer, OrderSerializer, \
    RestaurantSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'], )
    def in_cart(self, request, pk=None):
        serializer_context = {
            'request': request,
        }

        orders = OrderItem.objects.filter(status='c', customer=request.user)

        response = OrderItemSerializer(orders, many=True, context=serializer_context).data

        return Response(response, status.HTTP_200_OK)

    @action(detail=True, methods=['get'], )
    def ordered(self, request, pk=None):
        serializer_context = {
            'request': request,
        }

        orders = OrderItem.objects.filter(status='o', customer = request.user)

        response = OrderItemSerializer(orders, many=True, context=serializer_context).data

        return Response(response, status.HTTP_200_OK)


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(detail=True, methods=['get'], )
    def menu_list(self, request, pk=None):
        serializer_context = {
            'request': request,
        }

        restaurant = Restaurant.objects.get(pk=pk)
        menus = DishDetails.objects.filter(restaurant=restaurant)

        response = DishDetailsSerializer(menus, many=True, context=serializer_context).data

        return Response(response, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], )
    def orders(self, request, pk=None):
        serializer_context = {
            'request': request,
        }

        orders = OrderItem.objects.filter(status='o', item__restaurant_id=pk)
        print(orders)

        response = OrderItemSerializer(orders, many=True, context=serializer_context).data

        return Response(response, status.HTTP_200_OK)


class DishDetailsViewSet(viewsets.ModelViewSet):
    queryset = DishDetails.objects.all()
    serializer_class = DishDetailsSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }

        serializer = OrderItemSerializer(data=request.data)
        serializer.is_valid()
        obj = serializer.save(customer=request.user)
        return Response(OrderItemSerializer(obj, context=serializer_context).data, status.HTTP_201_CREATED)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer_context = {
            'request': request,
        }

        serializer = OrderSerializer(data=request.data)
        serializer.is_valid()
        obj = serializer.save(customer=request.user)

        for item in obj.items.all():
            item.status = 'o'
            item.save()

        return Response(OrderSerializer(obj, context=serializer_context).data, status.HTTP_201_CREATED)
