from chart.views import index
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
]
