
# se importa blueprint para ser utlizado.
from flask import Blueprint

# creacion de objeto blueprint 
equipo = Blueprint('equipo', __name__, template_folder='templates')

from . import routes