import uuid 
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db


class Author(db.Model):
    __tablename__ = "Author"
    author_id = db.Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4)
    author_name = db.Column(db.String(), nullable=False)

    books = db.relationship('Book', back_populates = "author", cascade="all")

    def __init__(self, author_name):
        self.author_name = author_name

    def new_author_obj():
        return Author("")


class AuthorSchema(ma.Schema):
    class Meta: 
        fields = ["author_id", "author_name", "books"]

    books = ma.fields.Nested ("BookSchema", many = True, only = ["book_id", "book_title"])


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many = True)