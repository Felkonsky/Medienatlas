from flask import render_template, request
from models import MediaStation



def register_routes(app, db):

    @app.route("/")
    def hello_world():
        return render_template("index.html")
    
    # @app.route("/<id")
    # def user(name):
    #     return str(db.query().all())
    
    @app.route("/mediastations")
    def mediastations():
        mediastations = db.MediaStation.query.all()
        return str(mediastations)
    
    