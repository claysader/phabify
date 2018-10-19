#phabify.py

from flask import Flask, request #import main Flask class and request object
import re
import json

app = Flask(__name__) #create the Flask app

@app.route('/', methods=['POST'])
def post_parse():

    text = request.form.get('text')
    user = request.form.get('user_name')

    pattern = "[Tt][0-9]{4}"
    matches = re.findall(pattern, text)
    linkText =  "Phab tickets detected: "

    if len(matches) > 0:
    	for match in matches:
    		phabLink = "https://phab.zenysis.com/" + match + " "
    		linkText = linkText + phabLink

    	x = {
    		"text": linkText
    	}

    	phabJson = json.dumps(x)	
    	
    	if user != 'slackbot':
    		return phabJson

    return Response(), 200