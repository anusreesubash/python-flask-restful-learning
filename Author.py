from flask_restful import Resource

class Author(Resource):
	def get(self):
		return {'message': 'GET Route was invoked'}

	def post(self):
		return {'message': 'POST Route was invoked'}

	def delete(self):
		return {'message': 'DELETE Route was invoked'}

	def put(self):
		return {'message': 'PUT Route was invoked'}