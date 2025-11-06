from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Author, Book, Borrower
from .serializers import AuthorSerializer, BookSerializer, BorrowerSerializer

# Create your views here.

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.select_related("author").all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BorrowerListCreateView(generics.ListCreateAPIView):
    queryset = Borrower.objects.select_related("book", "book__author").all()
    serializer_class = BorrowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
