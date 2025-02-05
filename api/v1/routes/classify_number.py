from flask_restful import Resource, abort, request
from flask import request, jsonify
import requests
from .utils import is_armstrong, is_odd, is_even, is_odd, is_perfect, is_prime

class ClassifyNumber(Resource):
    def get(self):
        try:
            number = request.args.get('number')
            print(number)
            if number is None:
                return {"number": None, "error": True }, 400
            number = int(number)
            print(number)
            response = requests.get(f"http://numbersapi.com/{number}/math") # Make request to Numbers API
            print(response.text)
            if response.status_code == 200:
                properties = []
                if is_armstrong.is_armstrong(number):
                    properties.append("armstrong")
                if is_even.is_even(number):
                    properties.append("even")
                if is_odd.is_odd(number):
                    properties.append("odd")
                return {
                        "number": number,
                        "is_prime": is_prime.is_prime(number),
                        "is_perfect": is_perfect.is_perfect(number),
                        "properties": properties,
                        "digit_sum": sum(int(digit) for digit in str(abs(number))),
                        "fun_fact": response.text
                        }
            raise Exception("Error in fetching data from Numbers API")
        except ValueError:
            return {"number": number, "error": True }, 400
        except Exception as e:
            abort(500, message=str(e))