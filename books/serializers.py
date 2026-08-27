from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'content', 'author', 'isbn', 'price',)

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError({
                'status': False,
                'message': 'Title must only contain letters, numbers and underscores.',
            })

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({
                'status': False,
                'message': 'Title already exists.',
            })

        return data

    def validate_price(self, attrs):
        if attrs<=0 or attrs>=999999:
            raise ValidationError({
                'status': False,
                'message': 'Price must be between 0 and 999999.',
            })