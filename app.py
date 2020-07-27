from flask import Flask
from flask_restful import Resource, Api

from Author import Author

app = Flask(__name__)
api = Api(app)

api.add_resource(Author,'/api/author')

app.run(port=5000, debug=True)