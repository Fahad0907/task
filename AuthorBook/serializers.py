from rest_framework import serializers
from AuthorBook import models as author_book_model


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = author_book_model.Author
        fields = ['id', 'name', 'date_of_birth']


class BookSerializer(serializers.ModelSerializer):
    author_obj = serializers.SerializerMethodField()
    class Meta:
        model = author_book_model.Book
        fields = ['id', 'author', 'title', 'publish_date', 'genre', 'author_obj']

    def get_author_obj(self, obj):
        try:
            author_instance = author_book_model.Author.objects.get(id=obj["id"])
            return author_instance.name
        except:
            return {}
