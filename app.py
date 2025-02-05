from flask import Flask, jsonify
from flask_restful import Api
from api.v1.routes.classify_number import ClassifyNumber

app = Flask(__name__)
app.json.sort_keys = False
api = Api(app)
api.add_resource(ClassifyNumber, '/api/classify-number')


if __name__ == '__main__':
    app.run(debug=True)