#servidor web
from flask import Flask
app = Flask(__name__)

@app.route("/")
def inicio():
    return ("Hola amigo")
if __name__ == "__main__":
    app.run()
    