from django.urls import path
from . import views as v

urlpatterns = [
    path('create/', v.ReviewCreateAPIView.as_view()),
    path('all', v.ReviewListAPIView.as_view()),
    path('<int:pk>/', v.ReviewDetailAPIView.as_view())
]
