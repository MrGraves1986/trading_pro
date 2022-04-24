from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('philosophy', views.philosophy),
    path('calculate', views.calculate),
    path('trade_setup', views.trade_setup),
    path('risk_management', views.risk),
    path('master', views.master),
    path('indicators', views.indicators),
]