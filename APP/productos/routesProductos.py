from flask import render_template, redirect, request

from . import producto

@producto.route('/productos' , methods=['GET', 'POST'])
def productos():
    return render_template('productos.html')