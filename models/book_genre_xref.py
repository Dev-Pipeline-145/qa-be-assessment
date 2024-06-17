from db import db

books_genres_xref = db.Table (
    "BooksGenresXref", 
    db.Model.metadata,
    db.Column("book_id",db.ForeignKey("Book.book_id",ondelete = "CASCADE"),primary_key = True),
    db.Column("genre_id",db.ForeignKey("Genre.genre_id",ondelete = "CASCADE"),primary_key = True)
)
