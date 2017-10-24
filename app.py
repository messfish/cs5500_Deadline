from database import db_session, init_db
from flask import Flask
from flask import request, jsonify, session
from os import environ
from flask_sqlalchemy import SQLAlchemy, inspect
from models import Pet
import json
# import models
# from models import engine, dbsession

__author__ = "Priyank Chaudhary"
__license__ = "MIT"
__credits__ = ["Priyank Chaudhary"]
__version__ = "0.1"
__status__ = "Production"

init_db()
app = Flask(__name__)
app.config.from_object(environ['APP_SETTINGS'])
# db = SQLAlchemy(app)

# TODO: move this to a configuration file.
config = {
    'auth': False  # enable authentication.
}


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def is_login_valid():
    return session.get('auth_email') is not None


@app.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def index():
    return "Welcome to Pet Project!"


@app.route("/_info")
def info():
    return jsonify({
        "Application": "flask-based-pet-project %s" % __version__,
    })


@app.route("/pet", methods=["POST"])
def add_pet():
    """TODO: Docstring for add_pet.
    :returns: TODO

    """
    data = request.get_json(force=True)
    print(data)
    to_write = Pet(**data)
    db_session.add(to_write)
    db_session.commit()
    return jsonify({"pet.id": to_write.id})


@app.route("/pet/<int:pet_id>", methods=["GET"])
def find_pet_by_id(pet_id):
    """TODO: Docstring for .

    :pet_id: TODO
    :returns: TODO

    """
    query_res = Pet.query.filter(Pet.id == pet_id).first()
    data = object_as_dict(query_res)
    return jsonify({"status": "success", "data": data})


@app.route("/pet/all/", methods=["GET"])
def find_all_known_pets():
    """TODO: Docstring for find_all_known_pets.
    :returns: TODO

    """
    query_res = Pet.query.all()
    data = [object_as_dict(r) for r in query_res]
    return jsonify({"status": "success", "data": data})


@app.route("/pet/<int:pet_id>/<string:place>", methods=["PUT"])
def move_pet_to_place(pet_id, place):
    """TODO: Docstring for .

    :place: TODO
    :pet_id: TODO
    :returns: TODO

    """
    query_res = Pet.query.filter(Pet.id == pet_id).first()
    data = object_as_dict(query_res)
    return jsonify({"status": "success", "data": data})


@app.route("/pet/<string:name>", methods=["GET"])
def find_pets_by_name(name):
    """TODO: Docstring for .

    :name: TODO
    :returns: TODO

    """
    query_res = Pet.query.filter(Pet._name == name).all()
    data = [object_as_dict(r) for r in query_res]
    return jsonify({"status": "success", "data": data})


@app.route("/pet/<string:kind>", methods=["GET"])
def find_pets_by_kind(kind):
    """TODO: Docstring for .

    :kind: TODO
    :returns: TODO

    """
    query_res = Pet.query.filter(Pet._kind == kind).all()
    data = [object_as_dict(r) for r in query_res]
    return jsonify({"status": "success", "data": data})


@app.route("/pet/<string:place>", methods=["GET"])
def find_pets_by_place(place):
    """TODO: Docstring for .

    :place: TODO
    :returns: TODO

    """
    query_res = Pet.query.filter(Pet._place == place).all()
    data = [object_as_dict(r) for r in query_res]
    return jsonify({"status": "success", "data": data})


@app.route("/pet/<string:color>", methods=["GET"])
def find_pets_by_color(color):
    """TODO: Docstring for .

    :color: TODO
    :returns: TODO

    """
    query_res = Pet.query.filter(Pet._color == color).all()
    data = [object_as_dict(r) for r in query_res]
    return jsonify({"status": "success", "data": data})


@app.route("/pet/<string:breed>", methods=["GET"])
def find_pets_by_breed(breed):
    """TODO: Docstring for .

    :breed: TODO
    :returns: TODO

    """
    query_res = Pet.query.filter(Pet._breed == breed).all()
    data = [object_as_dict(r) for r in query_res]
    return jsonify({"status": "success", "data": data})


@app.route("/pet/<string:gender>", methods=["GET"])
def find_pets_by_gender(gender):
    """TODO: Docstring for .

    :gender: TODO
    :returns: TODO

    """
    query_res = Pet.query.filter(Pet._gender == gender).first()
    data = [object_as_dict(r) for r in query_res]
    return jsonify({"status": "success", "data": data})


def object_as_dict(obj):
    return {
        c.key: getattr(obj, c.key)
        for c in inspect(obj).mapper.column_attrs
    }


# @app.route("/pet/<int:pet_id>/history", methods=["POST"])

# @app.route("/pet", methods=["POST"])

# @app.route("/pet", methods=["POST"])

# @app.route("/pet", methods=["POST"])
if __name__ == '__main__':
    print("pet project v%s" % __version__)
    app.secret_key = "some secret"
    app.debug = True
    app.run()
