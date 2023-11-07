# flask_6_api_management
The goal of this week's assignment is to develop, document, and manage APIs using Flask. You'll also explore the differences between the two frameworks and integrate your APIs with Azure API Management.


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

errors: 

flasgger: had to play around with parameters to get it to work otherwise the variables would show up as undefined and could not be edited
+ An error occurred trying to start process 'xdg-open' with working directory '/home/joyce_lin_1/flask_6_api_management/myapp'. No such file or directory
+app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS): anon makes it so anyone can access, function means it needs authentication 