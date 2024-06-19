from django.urls import path
from . import views as v

urlpatterns = [
    path('create/', v.CategoryCreateAPIView.as_view()),
    path('all', v.CategoryListAPIView.as_view()),
    path('<int:pk>/', v.CategoryDetailAPIView.as_view())
]
