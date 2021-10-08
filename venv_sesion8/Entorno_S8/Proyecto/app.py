from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hola Mundo 1'

@app.route('/saludo')
def saludo():
    return 'El otro Saludo'