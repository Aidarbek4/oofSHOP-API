from rest_framework import generics, permissions, status, response as res
from . import models as m, serializers as s


class ReviewListAPIView(generics.ListAPIView):
    queryset = m.Review.objects.all()
    serializer_class = s.ReviewSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = m.Review.objects.all()
    serializer_class = s.ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewDetailAPIView(generics.RetrieveAPIView):
    queryset = m.Review.objects.all()
    serializer_class = s.ReviewSerializer
