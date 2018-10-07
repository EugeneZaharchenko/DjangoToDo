
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('details/<int:id>', views.details),
    path('add/', views.add, name='add'),
    path('check/<int:id>', views.check, name='check'),
    path('uncheck/<int:id>', views.uncheck, name='uncheck'),
    path('delete/<task_id>', views.delete, name='delete'),
]
