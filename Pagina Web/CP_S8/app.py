from flask import Flask,render_template
app = Flask(__name__)

todos=['Manzana', 'Pera','Mango']

@app.route('/')
def index():
    return "<h1>Hola Tripulantes</h1>"

@app.route('/saludar')
def saludar():
    contexto={
        'title':'Sesión 8',
        'nombreM':'Maria !',
        'nombreH':'Pedro !',
        'saludo': '! Hola que tal',
        'tipo':1,
        'todos':todos
    }
    return render_template('hola_mundo.html', **contexto)
@app.route('/inicio')
def inicio():
    contexto={
        'title':'Sesión 8',
        'saludo2': 'Hola Tripulantes2',
        'saludo3': 'Hola Tripulantes3',
        'tipo':1,
    }
    return render_template('hola_mundo.html', **contexto)