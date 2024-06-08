# This is the practice program for the practice of ' requests library '

import requests as req

response = req.get('https://www.google.com')
print(response.status_code)
print(response.text)
