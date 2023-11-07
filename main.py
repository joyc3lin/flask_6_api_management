from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    return f"Hello from Joyce's Flask API Endpoint Server!"

@app.route('/hello', methods=['GET'])
def hello_get():
    """
    This endpoint returns a greeting message based on the information provided in the JSON body.
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: World
      - name: lastname
        in: query
        type: string
        required: false
        default: Lastname Not Provided
      - name: age
        in: query
        type: integer
        required: false
        default: 18
    responses:
      200:
        description: A greeting message
    """
    name = request.args.get('name', 'World')
    lastname = request.args.get('lastname', 'Lastname Not Provided')
    nameCapital = name.upper()
    lastnameCapital = lastname.upper()
    
    age = request.args.get('age', 18)
    age_real = int(age)
    age_analyzed = age_real - 18

    
    return jsonify(
        
        {'Greetings' : f'Hello {nameCapital} {lastnameCapital}!'}, 
        {'Age' : f'Your age is {age_analyzed} over 18. :)'}
        
        )


if __name__ == '__main__':
    app.run(debug=True)