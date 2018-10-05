
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('details/<int:id>/', views.details),
    path('add/', views.add, name='add'),
]
