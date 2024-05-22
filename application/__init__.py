from flask import Flask
from . import homepage
from .extensions import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]  = 'sqlite:///data.db'
    app.config["SECRET_KEY"] = 'A_SECRET'
    
    db.init_app(app)

    app.register_blueprint(homepage.bp)

    return app