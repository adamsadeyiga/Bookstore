from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# API views for ORM queries
@api_view(['GET'])
def books_by_author(request, author_id):
    books = Book.objects.filter(author_id=author_id)
    return Response({'books': [book.title for book in books]})

@api_view(['GET'])
def authors_with_books(request):
    print("authors_with_books view called")
    authors = Author.objects.annotate(book_count=Count('books')).filter(book_count__gt=0)
    return Response({'authors': [author.name for author in authors]})

@api_view(['GET'])
def most_recent_book(request):
    book = Book.objects.order_by('-publication_date').first()
    if book:
        return Response({'title': book.title, 'publication_date': book.publication_date})
    return Response({'message': 'No books found.'})
