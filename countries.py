from __future__ import print_function
import requests


import sys  # for sys.stderr.write()
import time  # for strftime

sys.stderr.write("Country App python script is starting up\n")
response=requests.get("https://restcountries.com/v2/all")
print(response.status_code)
for _ in response.json():
  print(_)