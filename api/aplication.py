import random
from flask import Flask, jsonify, make_response, request
from datetime import datetime

class Mensagem():
    def __init__(self, usuario, conteudo):
        self.usuario = usuario
        self.conteudo = conteudo
        self.data = datetime.now()
        
app = Flask(__name__)

messages = list()

@app.route("/messages", methods=['GET'])
def get_messages():

    data = list()
    for msg in messages:
        data.append({
            "usuario": msg.usuario,
            "conteudo": msg.conteudo,
            "data": msg.data
        })

    return make_response(jsonify(data))

@app.route("/messages", methods=['POST'])
def post_message():
    
    requestBody = request.json

    msg = Mensagem(requestBody['usuario'], requestBody['conteudo'])

    messages.append(msg)

    data = {
        "usuario": requestBody['usuario'],
        "conteudo": requestBody['conteudo']
    }

    return make_response(jsonify(data))
    
    