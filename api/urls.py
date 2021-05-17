from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'resturant', views.RestaurantViewSet)
router.register(r'dish', views.DishViewSet)
router.register(r'dish-avail', views.DishDetailsViewSet)
router.register(r'ord-item', views.OrderItemViewSet,)
router.register(r'order', views.OrderViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
