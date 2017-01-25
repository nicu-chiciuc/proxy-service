from rest_framework.fields import CharField
from rest_framework_mongoengine import serializers
from rest_framework_mongoengine import fields

from users.models import User


class UserSerializer(serializers.DocumentSerializer):

    class Meta:
        model = User
        fields = '__all__'
