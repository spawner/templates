import requests
import json
import base64

api_key = ''
addr = 'https://spawnerapi.com'
test_url = addr + '/image-classifier/' + api_key

# prepare headers for http request
content_type = 'image/jpeg'
headers = {'content-type': content_type}

# Base64 encode a PNG/JPEG image
b64 = base64.b64encode(open('lena.jpg','rb').read())

response = requests.post(test_url, data=b64, headers=headers)
# decode response
print(response.text)