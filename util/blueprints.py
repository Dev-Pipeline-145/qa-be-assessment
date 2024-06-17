import routes


def register_blueprints(app):
    app.register_blueprint(routes.authors)
    app.register_blueprint(routes.books)
    app.register_blueprint(routes.genres)