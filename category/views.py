from rest_framework import generics, permissions, status, response as res
from . import models as m, serializers as s


class CategoryListAPIView(generics.ListAPIView):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer


class CategoryCreateAPIView(generics.CreateAPIView):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Category.objects.all()
    serializer_class = s.CategorySerializer
