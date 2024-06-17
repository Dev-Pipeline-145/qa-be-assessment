from flask import Blueprint, request
import controllers 

genres = Blueprint("genres",__name__)

@genres.route("/genre",methods = ["POST"])
def add_genre():
    return controllers.add_genre(request)

@genres.route("/genres", methods = ["GET"])
def genres_get_all():
    return controllers.genres_get_all()

@genres.route("/genre/<genre_id>",methods = ["GET"])
def  genre_get_by_id(genre_id):
    return controllers.genre_get_by_id(genre_id)

@genres.route("/genre/<genre_id>", methods = ["PUT"])
def genre_update(genre_id):
    return controllers.genre_update(request, genre_id)

@genres.route("/genre/delete/<genre_id>", methods = ["DELETE"])
def genre_delete(genre_id):
    return controllers.genre_delete(genre_id)