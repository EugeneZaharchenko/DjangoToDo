
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('main/', views.main, name='main'),
    path('details/<int:x>', views.details),
    path('add/', views.add, name='add'),
    path('check/<task_id>', views.check, name='check'),
    path('uncheck/<task_id>', views.uncheck, name='uncheck'),
    path('delete/<task_id>', views.delete, name='delete'),
]
