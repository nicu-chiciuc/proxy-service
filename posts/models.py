from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import StringField, ReferenceField, ListField, EmbeddedDocumentField
from mongoengine.queryset.base import CASCADE

from users.models import User


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    comments = ListField(EmbeddedDocumentField(Comment))

    title = StringField(max_length=120, required=True)
    tags = ListField(StringField(max_length=30))

    meta = {
        'allow_inheritance': True
    }

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()