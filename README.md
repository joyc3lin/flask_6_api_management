# flask_6_api_management
The goal of this week's assignment is to develop, document, and manage APIs using Flask. You'll also explore the differences between the two frameworks and integrate your APIs with Azure API Management.

# Flask-based RESTful API

+ In Google Cloud Shell, create a python file with code take from the Professor's [app_flasgger.py](https://github.com/hantswilliams/HHA_504_2023/blob/main/WK6/code/flask/app_flasgger.py) file.
+ Edit code for personalization: [main.py](https://github.com/joyc3lin/flask_6_api_management/blob/main/main.py)

**To Run Flask-App**

+ Enter the directory where the python file is contained
+ Ensure FLask and Flasgger are installed
+ In the terminal, enter <code>python [file-name].py</code>
+ Click the link that generates that will lead to a new browswer tab
+ In the URL of the new tab, replace the part after ".cloudshell.dev/" with the app route name specified in the python file followed by a "?".

For example: 

```python
@app.route('/hello', methods=['GET'])
```
In this case, the app route name is "hello" and the url should look like "".cloudshell.dev/hello?"

+ This should return something like this:

![flaskapp1](https://github.com/joyc3lin/flask_6_api_management/blob/main/screenshots/flaskapp1.png)

+ To add other arguments in the URL after the "?", input the name of the argument, an equals sign, and then your input. To add more than one argument, separate the individual arguments with a "&" sign:

![flaskapp2](https://github.com/joyc3lin/flask_6_api_management/blob/main/screenshots/flaskapp2.png)


# Azure API deployment

# OpenAPI Specification and Documentation

+ create function func init LocalFunctionProj --python -m V2
+ install core packages tool: sudo apt-get install azure-functions-core-tools-4
+ pip install azure-functions
+ install azure cli: curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
(might take a while to download)
+ test install with az
+ login with: az login --use-device-code

To connect to azure storage account: 
+ create a azure atorage acc
+ under securty + access, access keys 
+ copy conenction string into local.setting.json "AzureWebJobsStorage"

+ https://joyceazureapp.azurewebsites.net/api/greeting

# Errors

flasgger: had to play around with parameters to get it to work otherwise the variables would show up as undefined and could not be edited
+ An error occurred trying to start process 'xdg-open' with working directory '/home/joyce_lin_1/flask_6_api_management/myapp'. No such file or directory
+ 
+ app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS): anon makes it so anyone can access, function means it needs authentication 
