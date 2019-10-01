# iniciando librerias
from flask import Flask, render_template
from horoscopo import HoroscopoChino
app = Flask(__name__)


# creando rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signo', methods=['POST'])
def signo():
    return render_template('signo.html')
