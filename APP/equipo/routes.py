#aqui se registra todos las rutas del tipo equipo. 
# importaciones de render_template con el cual trabaja a traves de jinja para el 
# texto plano .html y demas clases para la web
from flask import render_template, redirect, request

# del directorio actual importo el objeto blueprint para crear rutas
from . import equipo

@equipo.route('/equipo', methods=['GET', 'POST'])
def nuestroEquipo():
    return render_template('nuestroEquipo.html')