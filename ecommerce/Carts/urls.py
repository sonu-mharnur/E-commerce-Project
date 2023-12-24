
from django.urls import path
from .views import *
urlpatterns = [
    path('cart',cartView.as_view()),
]
