from mongoengine.document import Document, EmbeddedDocument
from mongoengine.fields import StringField, ReferenceField, ListField, EmbeddedDocumentField
from mongoengine.queryset.base import CASCADE

from users.models import User


class Comment(EmbeddedDocument):
    content = StringField()
    author = ReferenceField(User, required=False)


class Post(Document):
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    comments = ListField(EmbeddedDocumentField(Comment))

    title = StringField(max_length=120, required=True)
    tags = ListField(StringField(max_length=30))

    content = StringField(null=True)
    image_path = StringField(null=True)
    link_url = StringField(null=True)
