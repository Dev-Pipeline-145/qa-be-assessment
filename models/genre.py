import uuid 
import marshmallow as ma
from sqlalchemy.dialects.postgresql import UUID

from db import db
from models.book_genre_xref import books_genres_xref


class Genre(db.Model):
    __tablename__ = "Genre"
    genre_id = db.Column(UUID(as_uuid=True), primary_key=True, default = uuid.uuid4)
    genre_name = db.Column(db.String(), nullable=False)
 

    books = db.relationship('Book', back_populates='genres', secondary = books_genres_xref )


    def __init__(self, genre_name):
        self.genre_name = genre_name
        
    def new_genre_obj():
        return Genre("")

class GenreSchema(ma.Schema):
    class Meta: 
        fields = ["genre_id", "genre_name", "books"]

    books = ma.fields.Nested ("BookSchema", many = True, only = ["book_id", "book_title"])
   

genre_schema = GenreSchema()
genres_schema = GenreSchema(many = True)