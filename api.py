from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///RacingDB.db')
app = Flask(__name__)
api = Api(app)

class RaceType(Resource):
    """
    Define a route to return races by type
    """
    def get(self, r_type='Next+to+jump'):
        r_type = r_type.replace('+', ' ') # handle spaces
        conn = db_connect.connect() # connect to database
        query = conn.execute(f"select * from Race where type = '{r_type}'") # This line performs query and returns json result
        return {'Races': query.cursor.fetchall()} 

api.add_resource(RaceType, '/byType/<r_type>') # Route_1

if __name__ == '__main__':
     app.run(port='5002')