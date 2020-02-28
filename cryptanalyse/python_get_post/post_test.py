
# importing the requests library 
import requests 
  
# defining the api-endpoint  
API_ENDPOINT = "http://127.0.0.1/crypto_secu/bad_password.php?login=admin&password=password"
  
# your API key here 
API_KEY = ""
  
# your source code here 
source_code = ''' 
print("Hello, world!") 
a = 1 
b = 2 
print(a + b) 
'''
  
# data to be sent to api 
data = {'api_dev_key':API_KEY, 
        'api_option':'paste', 
        'api_paste_code':source_code, 
        'api_paste_format':'python'} 
  
# sending post request and saving response as response object 
r = requests.post(url = API_ENDPOINT, data = data) 
  
# extracting response text
print(r.text) 

