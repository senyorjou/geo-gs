from flask import Flask
from flask_httpauth import HTTPTokenAuth

from flask.ext.sqlalchemy import SQLAlchemy
from config import BaseConfig
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
ma = Marshmallow(app)
auth = HTTPTokenAuth(scheme='Token')

tokens = {
    "secret-token-1": "customer 1",
    "secret-token-2": "customer 2"
}