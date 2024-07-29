from flask import Blueprint, request
import controllers 

books = Blueprint("books",__name__)

@books.route("/book",methods = ["POST"])
def add_book():
    return controllers.add_book(request)

@books.route("/books", methods = ["GET"])
def books_get_all():
    return controllers.books_get_all()

@books.route("/book/<book_id>",methods = ["GET"])
def  book_get_by_id(book_id):
    return controllers.book_get_by_id(book_id)

@books.route("/book/<book_id>", methods = ["PUT"])
def book_update(book_id):
    return controllers.book_update(request,book_id)

@books.route("/book/delete/<book_id>", methods = ["DELETE"])
def book_delete(book_id):
    return controllers.book_delete(book_id)

@books.route("/book/add-genre", methods = ["PATCH"])
def book_add_genre():
    return controllers.book_add_or_remove_genre(request)

@books.route("/book/remove-genre", methods = ["PATCH"])
def book_remove_genre():
    return controllers.book_remove_genre(request)