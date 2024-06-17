from flask import jsonify, request

from db import db
from models.author import Author, authors_schema, author_schema

from util.reflection import populate_object


def add_author(request):
    post_data = request.form if request.form else request.json
    author_name = post_data.get ("author_name")

    author_query = db.session.query(Author).filter(Author.author_name == author_name).first()
    if author_query:
        return jsonify ({"message": "author already exists"}), 400 
    
    new_author = Author.new_author_obj()
    populate_object(new_author,post_data)

    db.session.add (new_author)
    db.session.commit()

    return jsonify ({"message": "author added", "results": author_schema.dump(new_author)}), 201

def authors_get_all():
    authors_query = db.session.query(Author).all()
    return jsonify ({"message": "authors found", "results": authors_schema.dump(authors_query)}), 200

def author_get_by_id(author_id):
    author_query = db.session.query(Author).filter(Author.author_id == author_id).first()
    return jsonify ({"message": "author found", "results": author_schema.dump(author_query)}), 200

def author_update(request, author_id):
    post_data = request.form if request.form else request.json

    author_query = db.session.query(Author).filter(Author.author_id == author_id).first()

    if author_query:
        populate_object(author_query, post_data)

        db.session.commit()

        return({"message": "author updated", "results": author_schema.dump(author_query)}), 200
    
    return jsonify({"message": "author not updated"}), 400


def author_delete(author_id):

    author_query = db.session.query(Author).filter(Author.author_id == author_id).first()
    
    if author_query:
        db.session.delete(author_query)
        db.session.commit()
        return jsonify({"message": "author deleted"}), 200
    
    return jsonify({"message": "author not found"}), 404