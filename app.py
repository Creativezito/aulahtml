from flask import (Flask, render_template, request,)

app = Flask(__name__)

@app.route("/", methods=("GET",))
def index():
    nome = request.args.get('nome')
    return f"""<h1>Página inicial</h1>
        <p>Olá {nome}, que nome bonito!
        """

@app.route("/galeria", methods=('GET',))
def galeria():
    return "<h1>Galeria</h1>"

@app.route("/contato", methods=('GET',))
def contato():
    return "<h1>Contato</h1>"

@app.route("/sobre", methods=('GET',))
def sobre():
    return "<h1>Sobre</h1>"

@app.route("/area/<float:largura>/<float:comprimento>", methods=('GET',))
def area(largura: float, comprimento: float):
    return f""" <h1>A área informada</h1>
    <p>A = {largura} * C = {comprimento} =>
    Área = {largura * comprimento}</p>"""

@app.route("/nomesobrenome/<string:nome>/<string:sobrenome>", methods=("GET",))
def nomesobrenome(nome, sobrenome):
    return f"""<h1>Nome e Sobrenome</h1>
        <p>Olá {sobrenome}, {nome}!
        """

@app.route("/potencial/<float:numero>/<float:potencia>", methods=('GET',))
def potencial(numero: float, potencia: float):
    return f"""<p>O Número: {numero} e a Potencia de {potencia} é equivalente a
    = {numero**potencia}</p>"""

@app.route("/tabuada")
@app.route("/tabuada/<numero>", methods=('GET',))
def tabuada (numero= None):

    if 'numero' in request.args:
        numero = int(request.args.get('numero'))

    return render_template('tabuada.html', numero=numero)

@app.route("/login")
def login(email = None, senha= None):
    if 'email' and 'senha' in request.args:
        email = request.args.get('email')
        senha = request.args.get('senha')
    
    return render_template('login.html', email=email, senha=senha)
    

