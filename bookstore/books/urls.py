from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, books_by_author, authors_with_books, most_recent_book

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/by-author/<int:author_id>/', books_by_author, name='books_by_author'),
    path('authors/with-books/', authors_with_books, name='authors_with_books'),
    path('books/most-recent/', most_recent_book, name='most_recent_book'),
]
