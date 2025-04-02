from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    return render_template('clientes.html')

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    return render_template('productos.html')

@app.route('/historial', methods=['GET', 'POST'])
def historial():
    return render_template('historial.html')
