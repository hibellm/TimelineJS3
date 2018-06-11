from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, validators
import requests
import json
import os
import codecs
import pandas as pd
from datetime import datetime
from elasticsearch import Elasticsearch
#from pymongo import MongoClient # Database connector
#from bson.objectid import ObjectId # For ObjectId to work

#APP settings
app = Flask(__name__,static_url_path='/static')


#CONNECT TO MONGODB
client = MongoClient('localhost', 32769)    #Configure the connection to the database
db = client.local                           #Select the database
tline = db.timeline                         #Select the collection

title = "Timeline Example"
heading = "Study Details"
#modify=ObjectId()

@app.route("/home")
def home():
	return render_template('index.html',t=title,h=heading)

@app.route("/tline")
def lists ():
    #Display the all Study data in the timeline
    #tline_l = tline.find()
    #print(tline_l)
    a1="active"
    return render_template('timeline.html',a1=a1,t=title,h=heading)

@app.route("/about")
def about():
	return render_template('credits.html',t=title,h=heading)


if __name__ == "__main__":
    app.secret_key='secret123'
    app.run('0.0.0.0',5005,debug=True)
