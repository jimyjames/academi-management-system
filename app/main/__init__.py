from flask import Blueprint

ams = Blueprint("ams", __name__)

from . import views