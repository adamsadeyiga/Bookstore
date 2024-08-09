from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'birth_date']

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_date', 'author']

    def create(self, validated_data):
        author = validated_data.pop('author')
        book = Book.objects.create(author=author, **validated_data)
        return book

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance
