from rest_framework import serializers
from .models import Post

class PostSearchSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Post
        fields = ('id', 'title', 'created')
        read_only_fields = ('id', 'title', 'created')