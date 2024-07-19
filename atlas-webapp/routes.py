from flask import render_template, request
from models import MediaStation, Exhibition, MediaContent, MediaType, Interaction
from werkzeug.utils import secure_filename

def register_routes(app, db):

    @app.route("/index")
    @app.route("/")
    def index():
        mediastations = MediaStation.query.all()
        
        return render_template("index.html", mediastations=mediastations)
    
    @app.route("/add-mediastation", methods=["GET", "POST"])
    def add():
        """Add form input to the database."""
        if request.method == "GET":
            return render_template("add-mediastation.html")
        elif request.method == "POST":
            
            # Mediastation
            ms_name = request.form.get("", type=str)
            ms_description = request.form.get("", type=str)
            
            # image_url = db.Column(db.Text)
            # path_to_exec = db.Column(db.Text)
            
            # Exibition
            ex_name = request.form.get("extitle", type=str)
            ex_location = request.form.get("exlocation", type=str)
            ex_start_date = request.form.get("exsdate", type=str)
            ex_end_date = request.form.get("exedate", type=str)
            ex_description = request.form.get("extrailer", type=str)
                        
            new_ex = Exhibition(title=ex_name, location=ex_location, start_date=ex_start_date, end_date=ex_end_date, trailer=ex_description)
            
            
            
            db.session.add(new_ex)
            db.session.commit()
            
            return render_template("add-mediastation.html")
        
    @app.route("/exhibitions")
    def get_exhibitions():
        exhibitions = Exhibition.query.all()
        
        return render_template("exhibitions.html", exhibitions=exhibitions)
    
    
    
    
    
    
        """OLD."""
    
        # img = request.files["mimage"]
        # path = request.files["msource"]
        
        # if not img or path:
        #     return "Keine Bild oder Pfad zur Medienstation angegeben", 400
        
        # filename_img = secure_filename(img.filename)
        # filename_path = secure_filename(path.filename)
        
        # mimetype_img = img.mimetype
        # mimetype_path = path.mimetype
        
        # # new_img = MediaStation(img=,)
        
        
    
    
    
    # @app.route("/<id")
    # def user(name):
    #     return str(db.query().all())
    
    # @app.route("/mediastations")
    # def mediastations():
    #     mediastations = db.MediaStation.query.all()
    #     return str(mediastations)
    