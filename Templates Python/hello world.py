# Importa as bibliotecas necessárias.
from flask import Flask, render_template

# Importa um módulo chamado 'test'.
import test

# Inicializa uma instância da aplicação Flask.
app = Flask(__name__)

# Rota que retorna uma mensagem "Hello World.py!"
@app.route("/")
def homepage():
    return "Hello World.py!"

# Rota que retorna uma mensagem "Starting..."
@app.route("/start")
def start():
    return "Starting..."

# Rota que renderiza um template HTML chamado usando a função render_template do Flask.
@app.route("/teste")
def lista_usuarios():
    return render_template("teste.html")

# Inicia o servidor Flask em modo de depuração.
app.run(debug=True)