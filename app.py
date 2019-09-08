from flask import Flask, request
from processCountries import processData
import json

app = Flask(__name__)

capitals = processData()


@app.route('/')
def hello():

    return ("Hello DataGrokr.! The API is https://sample-python-app-task.herokuapp.com/capital?country=India")



"""
This API will give the capital of the given country

The format is "https://sample-python-app-task.herokuapp.com/capital?country=%%%"
Replace the %%% in above url with the country name

Response is in the json with keys error and message

if error is true then either country name is not provided or incorrect country name


"""

@app.route('/capital' , methods=['GET'])
def getCapital():
	if request.args.get('country','') == "":
		return json.dumps({ 'error':True , 'message':"No country name provided"})

	if request.args.get('country','') in capitals:
		return json.dumps({ 'error':False , 'capital':capitals[request.args.get('country')]})
	else:
		return json.dumps({ 'error':True ,'message':"Invalid country name"})


if __name__ == '__main__':
	app.run()
