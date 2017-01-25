from rest_framework_mongoengine import serializers

from posts.models import Post, Comment
from users.models import User
from users.serializers import UserSerializer


class CommentSerializer(serializers.EmbeddedDocumentSerializer):
    author = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.DocumentSerializer):
    author = UserSerializer()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

    def _set_author(self, instance, author):
        instance.author = User.objects.get(**author).to_dbref()

    def _clear_comments(self, instance):
        instance.comments = []

    def _add_comments(self, instance, comments):
        for comment_data in comments:
            comment_author = comment_data.pop('author', None)
            comment_instance = Comment(**comment_data)
            self._set_author(comment_instance, comment_author)
            instance.comments.append(comment_instance)

    def create(self, validated_data):
        comments = validated_data.pop('comments', [])
        author = validated_data.pop('author', None)
        instance = super(PostSerializer, self).create(validated_data)

        self._set_author(instance, author)
        self._add_comments(instance, comments)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        comments = validated_data.pop('comments', [])
        validated_data.pop('author', None)
        instance = super(PostSerializer, self).update(instance, validated_data)

        self._clear_comments(instance)
        self._add_comments(instance, comments)

        instance.save()
        return instance
