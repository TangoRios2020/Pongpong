from flask import Blueprint

auth = Blueprint('auth_bp', __name__)

from . import views