import os

from flask import Flask, make_response, jsonify , request

from flask_cors import CORS

from app import db

import pymongo 




mongo = db.init_db()

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py', silent=True)

    
    db.get_db(mongo=mongo, app=app)

    from app.api import task

    app.register_blueprint(task.bp)




    return app
    
