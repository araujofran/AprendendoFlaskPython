from flask import Flask

app = Flask(__name__)

@app.route('/inicio')

def ola():
    return 'Olá Mundo!'

app.run()