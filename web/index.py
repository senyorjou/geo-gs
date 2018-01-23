from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from config import BaseConfig
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(BaseConfig)
db = SQLAlchemy(app)
ma = Marshmallow(app)
