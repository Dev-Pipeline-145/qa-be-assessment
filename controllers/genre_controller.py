from flask import jsonify, request

from db import db
from models.genre import Genre, genre_schema, genres_schema

from util.reflection import populate_object



def add_genre(request):
    post_data = request.form if request.form else request.json
    genre_name = post_data.get ("genre_name")

    genre_query = db.session.query(Genre).filter(Genre.genre_name == genre_name).first()
    if genre_query:
        return jsonify ({"message": "genre already exists"}), 400 
    
    new_genre = Genre.new_genre_obj()
    populate_object(new_genre,post_data)

    db.session.add (new_genre)
    db.session.commit()

    return jsonify ({"message": "genre added", "results": genre_schema.dump(new_genre)}), 201

def genres_get_all():
    genres_query = db.session.query(Genre).all()
    return jsonify ({"message": "genres found", "results": genres_schema.dump(genres_query)}), 200

def genre_get_by_id(genre_id):
    genre_query = db.session.query(Genre).filter(Genre.genre_id == genre_id).first()
    return jsonify ({"message": "genre found", "results": genre_schema.dump(genre_query)}), 200

def genre_update(request, genre_id):
    post_data = request.form if request.form else request.json

    genre_query = db.session.query(Genre).filter(Genre.genre_id == genre_id).first()

    if genre_query:
        populate_object(genre_query, post_data)

        db.session.commit()

        return({"message": "genre updated", "results": genre_schema.dump(genre_query)}), 200
    
    return jsonify({"message": "genre not updated"}), 400

def genre_delete(genre_id):

    genre_query = db.session.query(Genre).filter(Genre.genre_id == genre_id).first()
    
    if genre_query:
        db.session.delete(genre_query)
        db.session.commit()
        return jsonify({"message": "genre deleted"}), 200
    
    return jsonify({"message": "genre not found"}), 404