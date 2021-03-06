from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from ncdcapi import ncdc

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(ncdc,"/")

if __name__ == "__main__":
  app.run()
