from django.urls import include, path

from .views import *
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('currencies/', Currencies.as_view()),
    path('currency/<int:pk>/', Currency.as_view()),
    path('auth/register/', Register.as_view()),
    path('auth/login/', Login.as_view()),
]