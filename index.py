from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, send
import os
APP_DIR = os.path.abspath(os.path.dirname(__file__))
STATIC_FOLDER = os.path.join(APP_DIR, '/build') # Where your webpack build output folder is
TEMPLATE_FOLDER = os.path.join(APP_DIR, '/build') # Where your index.html file is located
app = Flask(__name__, static_folder=STATIC_FOLDER, template_folder=TEMPLATE_FOLDER, static_url_path='/')
# app.debug = True
app.config['SECRET_KEY'] = 'mysecret'

socketIo = SocketIO(app, cors_allowed_origins="*")

app.debug = True
app.host = 'localhost' 
@socketIo.on("message")
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)
    return None
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketIo.run(app)