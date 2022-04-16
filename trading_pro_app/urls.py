from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('philosophy', views.philosophy),
    path('calculate', views.calculate),
]