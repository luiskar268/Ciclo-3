from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def inicio():
    contexto={
        'titulo':"Sesión 9",
        'cuerpo':"Este es el body de mi página"
    }

    #return render_template('index.html', titulo="sesión 9",titulo='sesion 10')
    return render_template('index.html', **contexto)


@app.route('/productos/')
def listar_productos():
    return 'listar productos'


@app.route('/contactanos')
def contactanos():
    return 'contactanos'

@app.errorhandler(404)
def not_found(error):
    return 'La página no existe'

@app.route('/saludar')
@app.route('/saludar/<string:nombre>')
@app.route('/saludar/<string:nombre>/<int:edad>')
def saludar(nombre=None, edad=None):
    if nombre == None:
        return f'saludos a todos'
    else:
        if edad == None:
            return f'saludos {nombre}'
        return f'saludos {nombre} tienes {edad} años'

@app.route('/formulario', methods=["GET","POST"])
def recibir_fomulario():
    if request.method == 'GET':
        nombre = request.args.get('nombre')
        apellido = request.args.get('apellido')
        return f'Formulario GET nombre {nombre} y apellido {apellido}'
    else:
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        return f'Formulario POST nombre {nombre} y apellido {apellido}'
