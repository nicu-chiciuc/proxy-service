from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_mongoengine import viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from posts.models import Post
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = PostSerializer
    renderer_classes = (JSONRenderer, XMLRenderer)
    parser_classes = (JSONParser, XMLParser)

    def get_queryset(self):
        return Post.objects.all()
