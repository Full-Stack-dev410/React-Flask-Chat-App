from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__, static_folder = './build', static_url_path = '/')
app.config['SECRET_KEY'] = 'mysecret'

socketIo = SocketIO(app, cors_allowed_origins="*")

# app.debug = True
# app.host = 'localhost'git 
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