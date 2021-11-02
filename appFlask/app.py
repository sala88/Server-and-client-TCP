from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/")
def main():
    return render_template("index.html")


def test():
    for i in range(100):
        socketio.emit("test", i)
        socketio.sleep(1)        

if __name__ == '__main__':
    Thread(target=test).start()
    socketio.run(app)
