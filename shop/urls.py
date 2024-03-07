from itertools import product

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop import views
from shop.views import get_order

router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'product', views.ProductViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'cart', views.CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('order-count/<int:product_id/', get_order, name='order-count')
]