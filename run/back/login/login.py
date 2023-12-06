from config.config import path
from config.config import *
from config.cripto import *
from model.user import *


@app.route("/login", methods=['POST'])
def login():

    dados = request.get_json(force=True)  
    if dados["nome"] == "" or dados["senha"] == "": 
        return jsonify({"resultado":"erro", "detalhes":"Nome de usuario não pode ser vazio"})
    nome = dados['nome']
    senha = dados['senha']
    
    encontrado = Usuario.query.filter_by(nome=nome, senha=cifrar(senha)).first()

    if encontrado is None: 
        resposta = jsonify({"resultado": "erro", "detalhes":"usuario ou senha incorreto(s)"})

    else:
        # códigos HTTP:
        # https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status        

        # criar a json web token (JWT)
        access_token = create_access_token(identity=encontrado.id)
        resposta =  jsonify({"resultado":"ok", "detalhes":dict(token=access_token)})
    
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*") #meuservidor)
    # permitir envio do cookie
    #resposta.headers.add("Access-Control-Allow-Credentials", "true")

    return resposta 