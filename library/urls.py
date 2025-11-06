from django.urls import path
from . import views

urlpatterns = [
    path("authors/", views.AuthorListCreateView.as_view(), name="authors-list-create"),
    path("books/", views.BookListCreateView.as_view(), name="books-list-create"),
    path("borrowers/", views.BorrowerListCreateView.as_view(), name="borrowers-list-create"),
]
