import random
from flask import Flask, jsonify, make_response, request
from datetime import datetime

import mysqlx

db = mysqlx.connector.connect(
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
        self.data = datetime.now()
        
        
app = Flask(__name__)

messages = list()

@app.route("/messages", methods=['GET'])
def get_messages():
    cursor.execute('SELECT * FROM messages')
    messages = cursor.fetchall()
    data = list()
    for message in messages:
        data.append(
            {
                'usuario':message[1],
                'conteudo':message[2],
                'data':message[3]
            }
        )
    return make_response(jsonify(data), 200)

@app.route("/messages", methods=['POST'])
def post_message():
    
    requestBody = request.json
    cursor.execute(f"INSERT INTO messages (usuario, conteudo, msgDate) VALUES ('{requestBody['usuario']}', '{requestBody['conteudo']}', '{requestBody['msgDate']}')")
    data = {
        'usuario':requestBody['usuario'],
        'conteudo':requestBody['conteudo'],
        'msgDate':requestBody['msgDate']
    }

    return make_response(jsonify(data), 201)
    
    