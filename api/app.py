from flask import Flask, jsonify, request
import time
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    x ={
        "name": "John the first",
        "age": 30,
        "city": "New York"
    }
    return jsonify(
        x
    )

db = {"services":[{
        "address": "123 Fake Street, London, ABC 123",
        "id": "1",
        "name": "Tom's Garages",
        "distance": 0.5,
        "location": "London",
        "logo": "./../Services/Tom's Garages.png",
        "price": "££",
        "phone": "07746286271",
        "email": "tomsgarages@gmail.com",
        "stars": 3,
    },{
        "address": "123 Fake Street, London, ABC 123",
          "id": "2",
        "name": "Tom's Garages",
        "distance": 0.2,
        "location": "London",
        "logo": "./../Services/Tom's Garages.png",
        "price": "££",
        "stars": 3,
    },{
        "address": "123 Fake Street, London, ABC 123",
          "id": "3",
        "name": "Tom's Garages",
        "distance": 0.1,
        "location": "London",
        "logo": "./../Services/Tom's Garages.png",
        "price": "££",
        "stars": 3,
    }],
    "booked": []}


@app.route('/list', methods=['GET'])
def list():
    return jsonify(db)

@app.route('/getbyid/<id>', methods=['GET'])
def getbyid(id):
    service =  {
        key: [item for item in value if item.get("id") == id]
        for key, value in db.items()}
    return jsonify(service["services"][0])


@app.route('/filter', methods=['POST'])
def filter():
    data=request.json

    filtered_dict = {
    key: [item for item in value if item.get("location") == data["location"] and  item.get("price") in data["price"] and  item.get("stars") in data["stars"]]
    for key, value in db.items()
}


    # filtered_dict = {key: value for key, value in db.items() if value.get("location") == data["location"]}
    return jsonify(filtered_dict)


@app.route('/add', methods=['POST'])
def add():
    data = request.json
    db["booked"].append(data)
    # data["id"] = str(int(time.time()))
    # db[data["id"]] = data
    # return jsonify(db)
    return jsonify(data["bookingId"])

@app.route('/getbookingbyid/<id>', methods=['GET'])
def getbookingbyid(id):
    booking =  {
        key: [item for item in value if item.get("bookingId") == id]
        for key, value in db.items()}
    return jsonify(booking["booked"][0])


@app.route('/getbookings', methods=['GET'])
def getbookings():
    return jsonify(db["booked"])

@app.route('/update/<id>', methods=['POST'])
def update(id):

    for item in(db["booked"]):
        if item.get("bookingId") == id:
            i=db["booked"].index(item)
            break

    data = request.json
    db["booked"][i] = data
    return jsonify(db["booked"])

@app.route('/remove/<id>', methods=['POST'])
def remove(id): 
    for item in(db["booked"]):
        if item.get("bookingId") == id:
            i=db["booked"].index(item)
            break
    db["booked"].pop(i)
    return jsonify(db["booked"])

