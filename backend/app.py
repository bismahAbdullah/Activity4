from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://user15:12345678user@cluster0.jmc7smb.mongodb.net/")

db = client["test_db"]
collection = db["test"]

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    name = data['name']
    email = data['email']
    collection.insert_one({'name': name, 'email': email})
    return {'message': 'Data inserted successfully'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
