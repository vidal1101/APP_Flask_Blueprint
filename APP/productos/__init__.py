from flask import Blueprint

producto = Blueprint('productos', __name__, template_folder='templates')

from . import routesProductos