from flask import Flask, jsonify
from flask_restful import Api
from api.v1.routes.classify_number import ClassifyNumber
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)
api.add_resource(ClassifyNumber, '/api/classify-number')


if __name__ == '__main__':
    app.run()