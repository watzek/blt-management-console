from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/number')
def function_name():
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    return f"Hello, the number is {num1 * num2}"

