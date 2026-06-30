
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # VULNERABILIDAD: La entrada del usuario se inserta directamente en la respuesta HTML sin escapado
    user_input = request.args.get('input', '')
    return f'<h1>{user_input}</h1>'

if __name__ == "__main__":
    app.run()
