from main import app
from flask import render_template, flash, redirect, url_for
from app.forms import FormInicio
@app.route('/')
@app.route('/index')
def index():
    usuario = {'usuario':'...'}
    comentarios = [
        {
        'autor':{'usuario':'...'},
        'comentario':'...'
        },
        {
        'autor':{'usuario':'...'},
        'comentario':'...'
        }
    ]
    return render_template('index.html', titulo="Inicio", usuario=usuario,comentarios=comentarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = FormInicio()
    if(form.validate_on_submit()):
        flash('Inicio de sesión solicitado por el usuario {}, recordar={}'.format(form.usuario.data, form.recordar.data))
        return redirect(url_for('gracias'))
    return render_template('iniciar_sesion.html', form=form)

@app.route('/gracias')
def gracias():
    return render_template('gracias.html')