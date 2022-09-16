from flask import Flask 

app = Flask(__name__)

@app.route('/')
def simple_fn():
    return 'hello world!'