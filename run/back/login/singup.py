from config.config import *
from config.cripto import *
from model.user import *


@app.route("/cadastro", methods=['POST'])
def cadastro():
    resposta = jsonify({"resultado": "ok", "detalhes":" Usuario cadastrado"})
    dados = request.get_json(force=True)
    if dados["nome"] == "" or dados["senha"] == "": 
        return jsonify({"resultado":"erro", "detalhes":"Nome de usuario não pode ser vazio"})
    nome = dados['nome']
    senha = dados['senha']

    usuario = Usuario.query.filter_by(nome=nome, senha=cifrar(senha)).first()
    
    if usuario != None: 
        resposta = jsonify({"resultado": "erro", "detalhes":" Usuario já existente"})

    try: # tentar executar a operação
      nova = Usuario(nome=nome, senha=cifrar(senha))# criar a nova pessoa
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # ira mostrar o log
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!