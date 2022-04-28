import imp
from flask import Flask
from app.config import DevConfig
from flask_bootstrap import Bootstrap

app = Flask(__name__,instance_relative_config = True)
# Setup configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

bootstrap = Bootstrap(app) #How most extensions are intialized by passing app instance as parameter
from app import views
from app import error