from  flask import Flask
from .equipo import equipo
from .inicio import inicio


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config/configuration.cfg')
    app.register_blueprint(equipo)
    app.register_blueprint(inicio)
    return app
