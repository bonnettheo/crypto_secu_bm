# importing the requests library 
import requests 
  
# api-endpoint 
URL = "http://127.0.0.1/crypto_secu/bad_password.php?login=admin&password=password"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 

print(r.text)
  
# extracting data in json format 
# data = r.json() 
