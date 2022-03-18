import json

from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
from flask_mongoengine import MongoEngine
from mongoengine import connect
from mongoengine.connection import disconnect

from model import Users

app = Flask(__name__)
api = Api(app)

# connecting with Database
app.config['MONGO_URI'] = {'host': "mongodb://localhost:27017/test"}

db = MongoEngine(app)


class Register(Resource):
    def get(self):
        users = Users.objects()
        data = []
        for itr in users:
            data.append({"name": itr["Name"], "number": itr["PhoneNumber"]})
        print(data)
        return jsonify(data)

    def post(self):
        data = json.loads(request.data)
        users = Users(name=data['Name'], number=data['Number'])
        users.save()
        return {'message': 'User Registered', 'code': 201}


class Utility(Resource):
    def get(self, name):
        data = json.loads(request.data)
        users = Users.objects(name=name).first()
        result = {"Name": users.name, "PhoneNumber": users.number}
        return jsonify(result)

    def patch(self, name):
        data = json.loads(request.data)
        users = Users.objects(name=name).first()
        users.update(name=data['Name'], number=data["Number"])
        return {"message": "Data Updated", "code": 201}

    def delete(self, name):
        users = Users.objects(name=name).first()
        users.delete()
        return {"message": "Data Deleted", "code": 201}


api.add_resource(Register, '/register')
api.add_resource(Utility, '/utility/name')

if __name__ == "__main__":
    app.run(debug=True)
