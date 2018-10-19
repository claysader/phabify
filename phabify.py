#phabify.py

from flask import Flask, request #import main Flask class and request object
import re
import json

app = Flask(__name__) #create the Flask app

@app.route('/query-example')
def query_example():

	text = "I fixed T4523 and t8245"

	pattern = "[Tt][0-9]{4}"
	matches = re.findall(pattern, text)

	linkText =  "Phab tickets detected: "

	for match in matches:
		phabLink = "https://phab.zenysis.com/" + match + " "
		linkText = linkText + phabLink

	return linkText

@app.route('/test', methods=['POST'])
def form_example():
    return request

@app.route('/', methods=['POST'])
def json_parse():
#    req_data = request.get_json()

    text = request.form.get('text')
    user = request.form.get('user_name')

    pattern = "[Tt][0-9]{4}"
    matches = re.findall(pattern, text)
    linkText =  "Phab tickets detected: "

    if user != 'Phabify':
    	for match in matches:
    		phabLink = "https://phab.zenysis.com/" + match + " "
    		linkText = linkText + phabLink

    	x = {
    		"text": linkText
    	}

    	phabJson = json.dumps(x)	
    	
    	return phabJson 2

    return Response(), 200