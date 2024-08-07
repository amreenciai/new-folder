from flask import Flask, request, Response, make_response
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Invalid Request"

@app.route('/create_dataframe')
def create_dataframe():
    # Correct way to create a DataFrame
    df = pd.DataFrame([
        {'Name': 'lemon', 'color': 'yellow'},
        {'Name': 'apple', 'color': 'red'}
    ])

    # Create a response
    output = df.to_json(orient='records')
    response = make_response(output)
    response.headers['Content-Type'] = 'application/json'
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
