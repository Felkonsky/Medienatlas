from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

UPLOAD_FOLDER = '../data/'


db:SQLAlchemy= SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medienatlas.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['DATA_UPLOAD'] = UPLOAD_FOLDER
    
    db.init_app(app)
    
    # imports
    from routes import register_routes
    register_routes(app, db)
    
    migrate = Migrate(app, db)
    return app