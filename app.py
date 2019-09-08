from flask import Flask, request
from processCountries import processData
import json

app = Flask(__name__)

capitals = processData()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/capital' , methods=['GET'])
def getCapital():
	if request.args.get('country','') == "":
		return json.dumps({ 'error':True , 'message':"No country name provided"})

	if request.args.get('country','') in capitals:
		return json.dumps({ 'error':False , 'capital':capitals[request.args.get('country')]})
	else:
		return json.dumps({ 'error':True ,'message':"Invalid country name"})


if __name__ == '__main__':
	app.run(debug=True)
