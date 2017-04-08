from flask import Flask, request
import json


app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
  return "Hello this is cool"

