from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Product, Order, Cart
from .permissions import IsAdmin
from .serializers import CustomUserSerializer, ProductSerializer, OrderSerializer, CartSerializer


# Create your views here.

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdmin]

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

@swagger_auto_schema(
    method='get',
    #manual_parameters=[
    #    openapi.Parameter(
    #        name='search',
    #        in_=openapi.IN_QUERY,
    #        type=openapi.TYPE_STRING,
    #        description='Search query',
    #        required=False,
    #    ),
    #],
    responses={200: openapi.Response('Order view', serializer_name='Order serializer')},
)
@api_view(['GET'])
def get_order(request, product_id):
    product = Product.objects.get(pk=product_id)
    number_of_order = Order.objects.filter(product=product).count()

    return Response({'order': number_of_order})

