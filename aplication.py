from flask import Flask, jsonify, make_response, request
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sdchat"
)

cursor = db.cursor()

app = Flask(__name__)

@app.route("/messages", methods=['GET'])
def get_all():
    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()
    data = list()
    for message in messages:
        data.append({
            'user': message[0],
            'content': message[1],
            'msgDate': message[2]
        })
    return make_response(jsonify(data))

@app.route("/messages", methods=['POST'])
def post_message():
    requestBody = request.json
    cursor.execute(f'''INSERT INTO messages 
                   (user, content, msgDate) 
                   VALUES ('{requestBody['user']}', 
                   '{requestBody['content']}', 
                   '{requestBody['msgDate']}');''')
    data = {
        'user':requestBody['user'],
        'content':requestBody['content'],
        'msgDate':requestBody['msgDate']
    }
    return make_response(jsonify(data))