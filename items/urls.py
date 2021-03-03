from .views import item_list, item_detail
from django.urls import path


urlpatterns = [
    path('items/', item_list, name='item-list'),
    path('items/<int:pk>/', item_detail, name='book-detail'),
]