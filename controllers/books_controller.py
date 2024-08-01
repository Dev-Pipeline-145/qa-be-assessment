from flask import jsonify, request

from db import db
from models.books import Book, book_schema, books_schema
from models.genre import Genre

from util.reflection import populate_object

def add_book(request):
    post_data = request.form if request.form else request.json
    book_title = post_data.get ("book_title")

    book_query = db.session.query(Book).filter(Book.book_title == book_title).first()
    if book_query:
        return jsonify ({"message": "book title already exists"}), 400 
    
    new_book = Book.new_book_obj()
    populate_object(new_book,post_data)

    db.session.add (new_book)
    db.session.commit()

    return jsonify ({"message": "book added", "results": book_schema.dump(new_book)}), 201

def books_get_all():
    books_query = db.session.query(Book).all()
    return jsonify ({"message": "books found", "results": books_schema.dump(books_query)}), 200

def book_get_by_id(book_id):
    book_query = db.session.query(Book).filter(Book.book_id == book_id).first()
    return jsonify ({"message": "book found", "results": book_schema.dump(book_query)}), 200

def book_update(request, book_id):
    post_data = request.form if request.form else request.json

    book_query = db.session.query(Book).filter(Book.book_id == book_id).first()

    if book_query:
        populate_object(book_query, post_data)

        db.session.commit()

        return({"message": "book updated", "results": book_schema.dump(book_query)}), 200
    
    return jsonify({"message": "book not updated"}), 400

def book_delete(book_id):

    book_query = db.session.query(Book).filter(Book.book_id == book_id).first()
    
    if book_query:
        db.session.delete(book_query)
        db.session.commit()
        return jsonify({"message": "book deleted"}), 200
    
    return jsonify({"message": "book not found"}), 404

def book_add_or_remove_genre(request):
    post_data = request.form if request.form else request.json

    book_id = post_data.get("book_id")
    genre_id = post_data.get("genre_id")

    book_query = db.session.query(Book).filter(Book.book_id == book_id).first()

    if not book_query:
        return jsonify({"message": "book not found"}), 404
    
    genre_query = db.session.query(Genre).filter(Genre.genre_id == genre_id).first()

    if not genre_query:
        return jsonify({"message": "genre not found"},), 404

    if genre_query in book_query.genres:
        book_query.genres.remove(genre_query)
        db.session.commit()
        return jsonify({"message": "genre removed from book"},), 200
    else:
        book_query.genres.append(genre_query)
        db.session.commit()
        return jsonify({"message": "genre added to book"},), 200



    

