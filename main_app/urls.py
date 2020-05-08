from django.urls import path
from .views import index, AddItem, delete

urlpatterns = [
    path('', index),
    path('add/', AddItem.as_view(), name='add_item'),
    path('delete/<int:pk>', delete, name='delete_item'),   
]