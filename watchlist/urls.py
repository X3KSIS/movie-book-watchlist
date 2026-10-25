from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('add/', views.item_create, name='item_create'),
    path('edit/<int:pk>/', views.item_edit, name='item_edit'),
    path('done/<int:pk>/', views.mark_done, name='mark_done'),
]