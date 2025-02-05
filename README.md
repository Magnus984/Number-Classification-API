# Number Classification API

## Project Description

An API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Stack

- Flask
- Python

## Setup Instructions

1. Clone the repo:

    ```git clone https://github.com/Magnus984/Number-Classification-API```

2. Navigate to the project directory:

    ```cd BasicAPI```

3. Install the necessary requirements:

    ```pip install -r requirements.txt```

4. Run the application:

    ```python app.py```

5. Open your browser or API client and visit:

    ```http://127.0.0.1:5000//api/classify-number```

## API Endpoints

1. `GET /api/classify-number?number=371`
    - **Description**: Returns fun facts about number.

    - **Request Parameters**

    | Parameter | Type   | Required | Description |
    |-----------|--------|----------|-------------|
    | `number`  | `int`  | Yes      | The number to classify and retrieve facts for. |

    - **Response**: `{ "number": 371, "is_prime": false, "is_perfect": false, "properties": ["armstrong", "odd"], "digit_sum": 11, "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371" }`
    - **Example usage**: `curl https://magnus984.pythonanywhere.com/api/classify-number?number=371`
