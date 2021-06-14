from flask import render_template, redirect, request

from . import inicio

@inicio.route('/',methods=['GET'])
@inicio.route('/inicio', methods=['GET','POST'])
def inicio():
    return render_template('index.html')