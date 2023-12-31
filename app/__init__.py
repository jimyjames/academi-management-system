from flask import Flask
from config import  config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from datetime import datetime

db= SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_name):
    app= Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)

    bootstrap.init_app(app)


    from .main import ams as ams_blueprint
    app.register_blueprint(ams_blueprint)

    return app
