#importaciones 
# app: This module implements the central WSGI application object.

from flask import app
from APP import create_app

app = create_app()
app.run(port=5000, debug=True  )