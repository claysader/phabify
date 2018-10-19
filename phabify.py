#phabify.py

from flask import Flask, request #import main Flask class and request object
import re

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
def query_example():

	text = "I fixed T4523"

	pattern = "[Tt][0-9]{4}"
	matches = re.findall(pattern, text)

	linkText =  "Phab tickets detected: "

	for match in matches:
		phabLink = "phab.zenysis.com/" + match + " "
		linkText = linkText + phabLink

    return linkText

@app.route('/form-example')
def form_example():
    return 'Todo...'

@app.route('/json-example')
def json_example():
    return 'Todo...'