from rest_framework.filters import OrderingFilter, SearchFilter

from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import ProductSerializer
from .models import Product


class ProductListAPIView(ListAPIView):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category', 'on_sale']
    search_fields = ['title']
    ordering_fields = ['title', 'price']

    def get_queryset(self):
        queryset = Product.objects.filter(is_published=True) \
            .select_related('category')
        return queryset
