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

+ Instructions for deployment to Azure can be found [here](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=linux%2Cbash%2Cazure-cli&pivots=python-mode-decorators)
+ First, install Azure CLI in the terminal with <code>curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash</code>
  + This may take a while to download
+ To test if Azure has been installed, use: <code>az</code>
+ Log into Azure with: <code>az login --use-device-code</code>
+ Select URL provided
+ Copy paste code provided in the same line as URL
+ Pick an account
+ Select "Yes" to the prompt "Are you trying to sign in to Microsoft Azure CLI?"
+ Install the Core Tools package in terminal with: <code>sudo apt-get install azure-functions-core-tools-4</code>
  + also <code>pip install azure-functions</code>

</br>

**Creating Function Project**

+ Create a new function project with: <code>func init [name-of-project] --python -m V2</code>
+ <code>cd [name-of-project]</code> into the project folder
+ The folder will come with files such as <code>local.settings.json</code>,  <code>function_app.py</code>, and <code>.gitignore</code>
  + <code>local.settings.json</code> contains important configuration information and has been placed into the <code>.gitignore</code> file and won't show in a GitHub Repository
  + <code>function_app.py</code> is where the code for the azure app will he held
+ To start, go to <code>function_app.py</code> and replace the code with:

```python
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HttpExample")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("HttpExample function processed a request!")
```
+ The code can then be edited for personalization: [function_app.py](https://github.com/joyc3lin/flask_6_api_management/blob/main/myapp/function_app.py)
+ Ensure that in <code>local.settings.json</code>, <code>AzureWebJobsFeatureFlags</code> has been set to <code>EnableWorkerIndexing</code>
+ Also in <code>local.settings.json</code>, update so that <code>AzureWebJobsStorage</code> has been set to <code>"UseDevelopmentStorage=true"</code>

</br>

**To Create Azure Resources**

+ First, create an Azure resource group with:

```python
az group create --name [RESOURCE_GROUP_NAME] --location [REGION]
```
_Replace [RESOURCE_GROUP_NAME] and [REGION] with selected name and location_

</br>

+ Then, create a storage account within the resource group and region with:

```python
az storage account create --name [STORAGE_NAME] --location [REGION] --resource-group [RESOURCE_GROUP_NAME] --sku Standard_LRS
```
_Replace [STORAGE_GROUP] with selected name for storage container_

</br>

+ Lastly, create a function app with:

```python
az functionapp create --resource-group [RESOURCE_GROUP_NAME] --consumption-plan-location [REGION] --runtime python --runtime-version 3.9 --functions-version 4 --name [APP_NAME] --os-type linux --storage-account [STORAGE_NAME]
```
_Replace [APP_NAME] with selected name for the function app that will also show in the app's URL_

</br>

**Deploying Project to Azure**

+ To r
# OpenAPI Specification and Documentation

+ create function func init LocalFunctionProj --python -m V2


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
