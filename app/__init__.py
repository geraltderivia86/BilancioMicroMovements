from flask import Flask
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
api = Api(app,
       version='0.1',
       title='Api Bilacio Personale Movements',
       description='api Bilancio personale gestione Controllers movimenti',
       endpoint='api')

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://aymxzpntzvnvgx:e5ee99cf7eb02eed0c3b4002b82ba28c2f2e3efa226323f558768c67b2542816@ec2-54-247-89-181.eu-west-1.compute.amazonaws.com:5432/d5hh16cpa2bt0p'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import movements

api.add_namespace(movements)