from flask import render_template, redirect, request

from . import equipo

@equipo.route('/equipo', methods=['GET', 'POST'])
def nuestroEquipo():
    return render_template('nuestroEquipo.html')