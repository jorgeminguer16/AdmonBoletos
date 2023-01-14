from flask import Flask
from app.config import DATABASE_CONNECTION_URI
from app.api.events import EventController
from app.api.tickets import TicketController


def init_db(app : Flask):
    from app.models import db
    db.init_app(app)

def register_models():
    from app.models.event import Event, Ticket


def register_apis(app: Flask):
    app.register_blueprint(EventController)
    app.register_blueprint(TicketController)

def create_app():
    app = Flask(__name__)

    app.secret_key = 'mysecret'
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # no cache
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    register_apis(app)

    init_db(app)

    register_models()

    return app