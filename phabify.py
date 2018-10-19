#phabify.py

from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/phabify', methods=['POST']) #GET requests will be blocked
def phabify():
    return 'Todo...