from flask import Flask, jsonify
from pymongo import MongoClient
monngo = MongoClient('mongodb+srv://test:test@cluster0-onecv.mongodb.net/test?retryWrites=true&w=majority')
#creating Cliet
app = Flask(__name__)