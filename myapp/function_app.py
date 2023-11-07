import azure.functions as func
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="Example")
@app.route(route="greeting")
def greeting(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name', 'World')
    lastname = req.params.get('lastname', 'Lastname Not Provided')
    nameCapital = name.upper()
    lastnameCapital = lastname.upper()

    age = req.params.get('age', 18)
    age_real = int(age)
    age_analyzed = age_real - 18    


    return func.HttpResponse(
        json.dumps(
        {'Greetings' : f'Hello {nameCapital} {lastnameCapital}!', 
        'Age' : f'Your age is {age_analyzed} over 18. :)'}
        ),        
        status_code=200
        )