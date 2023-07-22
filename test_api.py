
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask_ngrok import run_with_ngrok
import pickle
import urllib.request

import requests
import json

app = Flask(__name__)



@app.route('/')
def home():

    return render_template("index.html")

@app.route('/predict',methods=['GET'])
def predict():
  '''
  For rendering results on HTML GUI
  '''
  income = int(request.args.get('income'))
  score = int(request.args.get('score'))
  # Serialize the data into json and send the request to the model
  X=[[income,score]]
  payload = {'data': json.dumps(X)}
  predict = requests.post('http://127.0.0.1:5000/kmeans', data=payload).json()


  
  if predict==[0]:
    result="Customer is Standard"

  elif predict==[1]:
    result="Customer is Target"
  elif predict==[2]:
    result="Customer is Sensible"
  elif predict==[3]:
    result="Customer is Careless"

  else:
    result="Custmor is Carefull"


  return render_template('index.html', prediction_text='Model  has predicted  : {}'.format(result))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
