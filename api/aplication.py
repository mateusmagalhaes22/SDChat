import random
from flask import Flask, jsonify, make_response, request
from datetime import datetime

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sdchat"
)

cursor = db.cursor()

class Mensagem():
    def __init__(self, usuario, conteudo):
        self.usuario = usuario
        self.conteudo = conteudo
        self.msgDate = datetime.now()
        
        
app = Flask(__name__)

@app.route("/messages", methods=['GET'])
def get_messages():
    cursor.execute('SELECT * FROM messages')
    messages = cursor.fetchall()
    data = list()
    for message in messages:
        data.append(
            {
                'usuario':message[0],
                'conteudo':message[1],
                'msgDate':message[2]
            }
        )
    return make_response(jsonify(data), 200)

@app.route("/messages", methods=['POST'])
def post_message():
    
    requestBody = request.json
    msg = Mensagem(requestBody['usuario'], requestBody['conteudo'])
    cursor.execute(f"INSERT INTO messages (usuario, conteudo, msgDate) VALUES ('{msg.usuario}', '{msg.conteudo}', '{msg.msgDate}')")
    data = {
        'usuario':msg.usuario,
        'conteudo':msg.conteudo,
        'msgDate':msg.msgDate
    }

    return make_response(jsonify(data), 201)
    
    