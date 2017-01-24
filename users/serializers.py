from rest_framework_mongoengine import serializers

from users.models import User


class UserSerializer(serializers.DocumentSerializer):
    class Meta:
        model = User
        fields = '__all__'
