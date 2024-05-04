from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class BookDetail(APIView):
    def get(self, request, name):
        try:
            book = Book.objects.get(name__iexact=name)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:   
            return Response({"message": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
