from rest_framework import serializers
from .models import Author, Book, Borrower
from django.db import transaction
from rest_framework.exceptions import ValidationError

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "email"]

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Author.objects.all(), source="author"
    )

    class Meta:
        model = Book
        fields = ["id", "title", "author", "author_id", "published_date", "available_copies"]

class BorrowerSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Book.objects.all(), source="book"
    )

    class Meta:
        model = Borrower
        fields = ["id", "name", "email", "book", "book_id", "borrowed_date", "return_date"]
        read_only_fields = ["borrowed_date"]

    def validate(self, attrs):
        # attrs contains 'book' (after source mapping)
        book = attrs.get("book") or getattr(self.instance, "book", None)
        if book and book.available_copies <= 0:
            raise ValidationError({"book_id": "No available copies to borrow."})
        return attrs

    def create(self, validated_data):
        book = validated_data["book"]
        # Use transaction to ensure available_copies decremented atomically
        with transaction.atomic():
            book = Book.objects.select_for_update().get(pk=book.pk)
            if book.available_copies <= 0:
                raise ValidationError({"book_id": "No available copies to borrow."})
            book.available_copies -= 1
            book.save()
            borrower = Borrower.objects.create(**validated_data)
        return borrower
