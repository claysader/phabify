#phabify.py

from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/phabify', methods=['POST']) #GET requests will be blocked
def phabify():
    return 'Todo...'

@app.route('/query-example')
def query_example():
    return 'Todo...'

if __name__ == '__main__':
    app.run() #run app in debug mode on port 5000