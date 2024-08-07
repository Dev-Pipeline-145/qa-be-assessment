from flask import Flask
from flask_cors import CORS
import os

from flask_marshmallow import Marshmallow

from db import *
from util.blueprints import register_blueprints
from lib.demo_data import add_demo_data


flask_host = os.environ.get("FLASK_HOST")
flask_port = os.environ.get("FLASK_PORT")

database_scheme = os.environ.get("DATABASE_SCHEME")
database_user = os.environ.get("DATABASE_USER")
database_address = os.environ.get("DATABASE_ADDRESS")
database_port = os.environ.get("DATABASE_PORT")
database_name = os.environ.get("DATABASE_NAME")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{database_scheme}{database_user}@{database_address}:{database_port}/{database_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)
ma = Marshmallow(app)

register_blueprints(app)


def create_tables():
    with app.app_context():
        print("creating tables...")
        db.create_all()
        print("tables created successfully")


CORS(app)
create_tables()


if __name__ == "__main__":
    with app.app_context():
        add_demo_data()
        
    app.run(host=flask_host, port=flask_port)
