from rest_framework import mixins
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework_mongoengine import viewsets
from rest_framework_mongoengine.generics import GenericAPIView
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''
    Contains information about inputs/outputs of a single program
    that may be used in Universe workflows.
    '''
    lookup_field = 'id'
    serializer_class = UserSerializer
    renderer_classes = (JSONRenderer, XMLRenderer)
    parser_classes = (JSONParser, XMLParser)

    def get_queryset(self):
        return User.objects.all()
