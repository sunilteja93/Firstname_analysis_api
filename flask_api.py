from flask import Flask, request
import flask_restful as restful
from flask_restful import Resource, Api, reqparse
from utils import Utils

app = Flask(__name__)
api = Api(app)

class Firstname_analysis(Resource):
		
	## Get method	
	def get(self):
		firstname = request.args.get('firstname')	
		dob = request.args.get('dob')
		
		## Base condition
		if not firstname and not dob:
			return "Please enter valid input"
		util = Utils()
		return (util.nameanalysis_report(dob, firstname))


api.add_resource(Firstname_analysis, '/nameanalysis')

if __name__ == '__main__':
    app.run()  # run our Flask app