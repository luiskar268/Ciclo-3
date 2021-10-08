from flask import Flask

app = Flask(__name__)

#from app import rutas

#@app.errorhandler(404)
def not_found(error):
    return '<h1>La página no existe</h1>'