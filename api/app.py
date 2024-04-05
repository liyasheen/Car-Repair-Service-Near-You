from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    return jsonify(
        x
    )