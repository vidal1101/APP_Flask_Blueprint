
#contrcutor de inicio de la app 
# se intancia los objetos blueprint y se registra
from  flask import Flask
from .equipo import equipo
from .inicio import inicio
from .productos import producto

# se encapsula todo en un metodo para dar el arranque de la app 
def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/configuration.cfg')
    app.register_blueprint(equipo)
    app.register_blueprint(inicio)
    app.register_blueprint(producto)
    return app
