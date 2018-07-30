# api/views.py

from rest_framework import generics
from .serializers import PostSearchSerializer
from .models import Post


class PostSearch(generics.ListAPIView):
    serializer_class = PostSearchSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Post.objects.all()
        q = self.request.query_params.get('q', None)
        if q is not None:
            queryset = queryset.filter(title__contains=q)
        return queryset    
