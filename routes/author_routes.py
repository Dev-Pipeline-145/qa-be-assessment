from flask import Blueprint, request
import controllers 

authors = Blueprint("authors",__name__)

@authors.route("/author",methods = ["POST"])
def add_author():
    return controllers.add_author(request)

@authors.route("/authors", methods = ["GET"])
def authors_get_all():
    return controllers.authors_get_all()

@authors.route("/author/<author_id>",methods = ["GET"])
def  author_get_by_id(author_id):
    return controllers.author_get_by_id(author_id)

@authors.route("/author/<author_id>", methods = ["PUT"])
def author_update(author_id):
    return controllers.author_update(request,author_id)

@authors.route("/author/delete/<author_id>", methods = ["DELETE"])
def author_delete(author_id):
    return controllers.author_delete(author_id)