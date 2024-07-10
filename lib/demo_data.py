from models.genre import Genre
from models.author import Author

from db import db

def add_demo_data():
    genres = [
        Genre(
            genre_name= "Action"
        ), 
        Genre(
            genre_name= "Mystery"
        ),
        Genre(
            genre_name="Science"
        ),
        Genre(
            genre_name="Fiction"
        )
    ]

    authors = [ 
        Author (
            author_name= "J.K. Rowling"
        ), 
        Author (
            author_name= "Stephen King"
        ),
        Author (
            author_name= "Sarah J. Maas"
        ),
        Author (
            author_name= "Agatha Christie"
        )
    ]

    db.session.bulk_save_objects(genres)
    db.session.bulk_save_objects(authors)

    db.session.commit()
