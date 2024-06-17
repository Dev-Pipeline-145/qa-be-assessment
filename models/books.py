

import uuid 
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db
from models.book_genre_xref import books_genres_xref


class Book(db.Model):
    __tablename__ = "Book"
    book_id = db.Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4)
    book_title = db.Column(db.String(), nullable=False)
    author_id = db.Column(UUID(as_uuid=True), db.ForeignKey('Author.author_id'), nullable=False)

    author = db.relationship('Author', back_populates = "books")
    genres = db.relationship('Genre', back_populates='books', secondary = books_genres_xref )


    def __init__(self, book_title, author_id):
        self.book_title = book_title
        self.author_id = author_id
        
    def new_book_obj():
        return Book("", "")

class BookSchema(ma.Schema):
    class Meta: 
        fields = ["book_id", "book_title", "author", "genres"]

    author = ma.fields.Nested ("AuthorSchema", only = ["author_id", "author_name"])
    genres = ma.fields.Nested ("GenreSchema", many = True, only = ["genre_id", "genre_name"])


book_schema = BookSchema()
books_schema = BookSchema(many = True)