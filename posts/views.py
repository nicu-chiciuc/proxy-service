from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

from posts.models import Post
from posts.serializers import PostSerializer
from users.models import User


class PostViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all()

    def _assign_author(self, instance, author):
        instance.author = User.objects.get(**author).to_dbref()
        instance.save()
        return instance

    def _create(self, request, *args, **kwargs):
        author = request.data.pop('author', None)
        # if author is not None:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.serializer.instance = self._assign_author(self.serializer.instance, author)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data,  status=status.HTTP_201_CREATED, headers=headers)