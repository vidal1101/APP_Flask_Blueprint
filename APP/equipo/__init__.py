from flask import Blueprint

equipo = Blueprint('equipo', __name__, template_folder='templates')

from . import routes