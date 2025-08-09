from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
        
    def validate(self, value):
        current_year =datetime.now().year
        
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
        