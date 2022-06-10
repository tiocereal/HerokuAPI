#FEITO POR NEODOUGLAS - ねおどうが#7773
import email
from flask import *
import os
import samino
os.system('set FLASK_ENV=development')
app = Flask(__name__)


@app.route('/api/login')
def get_timezone():
  data = request.args
  email = data.get("email")
  password = data.get("password")
  device = data.get("device")
  client = samino.Client(deviceId = device)
  client.login(email = email, password = password)
  print(client.sid)
  return f"{client.sid}"

if __name__ == '__main__':
  app.run("0.0.0.0", 5000)

import requests 
