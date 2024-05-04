from django.urls import path
from .views import BookDetail

urlpatterns = [
    path('books/<str:name>/', BookDetail.as_view(), name='book-detail'),
]
