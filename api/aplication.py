import random
from flask import Flask, jsonify, make_response, request
from datetime import datetime

class Mensagem():
    def __init__(self, usuario, conteudo):
        self.usuario = usuario
        self.conteudo = conteudo
        self.data = datetime.now()
        

class Room():
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.mensagens = []

app = Flask(__name__)

rooms = list()

@app.route("/rooms", methods=['GET'])
def get_all_rooms():
    
    data = []

    for room in rooms:
        data.append({
            'id': room.id,
            'nome': room.nome
            })
    return make_response(jsonify(data))

@app.route("/rooms", methods=['POST'])
def post_room():
    requestBody = request.json

    ids = []
    for i in range(0, 30):
        ids.append(i)
    for room in rooms:
        ids.pop(room.id)
    
    if len(ids) == 0:
        return make_response(jsonify({'error': "não é possivel criar mais salas"}))

    roomId = random.randint(ids[0], ids[-1])

    room = Room(roomId, requestBody['nome'], requestBody['senha'])

    rooms.append(room)

    data = {
        'nome':requestBody['nome']
    }

    return make_response(jsonify(data))

@app.route("/rooms/<id>", methods=['GET'])
def get_messages(id):
    id = int(request.view_args['id'])
    data = []
    for room in rooms:
        if room.id == id:
            for msg in room.mensagens:
                data.append({
                    'usuario': msg.usuario,
                    'conteudo': msg.conteudo,
                    'dataMsg': msg.data
                })
            break

    return make_response(jsonify(data))

@app.route("/rooms/<id>", methods=['POST'])
def post_message(id):
    
    requestBody = request.json

    id = int(request.view_args['id'])

    msg = Mensagem(requestBody['usuario'], requestBody['conteudo'])

    data = {
        "usuario": requestBody['usuario'],
        "conteudo": requestBody['conteudo']
    }
    for room in rooms:
        if room.id == id:
            room.mensagens.append(msg)
            break

    return make_response(jsonify(data))
    
    