import os
from flask_wtf import FlaskForm
# from forms import UploadForm
from flask import request,render_template, flash, redirect, send_from_directory, url_for
from models import MediaStation, Exhibition, MediaContent, MediaType, Interaction, Visualization
# , mt_audio, mt_image, mt_object, mt_text, mt_video, it_compare, it_connect, it_point_and_click, it_focus, it_move, it_touch, it_zoom, viz_book, viz_glyph, viz_map, viz_slideshow, viz_tiles, viz_timeline
from werkzeug.utils import secure_filename
# from app import ms_data, ms_images

def register_routes(app, db):
    """Routing and db related stuff."""
    ################
    # Static Types #
    ################

    # Media types
    mt_audio = MediaType(name="Audio")
    mt_video = MediaType(name="Video")
    mt_image = MediaType(name="Bilder")
    mt_text = MediaType(name="Text")
    mt_object = MediaType(name="3D Objekt")

    # Interaction types
    it_zoom = Interaction(name="Vergrößern")
    it_compare = Interaction(name="Vergleichen")
    it_point_and_click = Interaction(name="Zeigen und Klicken")
    it_touch = Interaction(name="Berühren")
    it_connect = Interaction(name="Verknüpfen")
    it_move = Interaction(name="Bewegen")
    it_focus = Interaction(name="Fokussieren")

    # Interactive Visualization realization
    viz_slideshow = Visualization(name="Diashow")
    viz_glyph = Visualization(name="Glyphen")
    viz_timeline = Visualization(name="Zeitstrahl")
    viz_map = Visualization(name="Karte")
    viz_book = Visualization(name="Buch")
    viz_tiles = Visualization(name="Kacheln")
    
    
    type_dict = {
        "media": {
            "audio": mt_audio,
            "video": mt_video,
            "image": mt_image,
            "text": mt_text,
            "object": mt_object
        },
        "interaction": {
            "compare": it_compare,
            "connect": it_connect,
            "focus": it_focus,
            "move": it_move,
            "pointclick": it_point_and_click,
            "touch": it_touch,
            "zoom": it_zoom
        },
        "visualization": {
            "book": viz_book,
            "glyph": viz_glyph,
            "map": viz_map,
            "slideshow": viz_slideshow,
            "tiles": viz_tiles,
            "timeline": viz_timeline
        }
    }
    
    @app.route("/index")
    @app.route("/")
    def index():
        mediastations = MediaStation.query.all()
        mediatypes = MediaType.query.all()
        interactions = Interaction.query.all()
        visualizations = Visualization.query.all()
        
        return render_template("index.html", mediastations=mediastations, interactions=interactions, visualizations=visualizations)
    
    @app.route("/uploads/images/<img>")
    def get_image(img):
        return send_from_directory(app.config["IMG_UPLOAD"], img)
    
    @app.route("/uploads/data/<data>")
    def get_data(data):
        return send_from_directory(app.config["DATA_UPLOAD"], data)
    
    @app.route("/add-mediastation", methods=["GET", "POST"])
    def add():
        """Insert add-mediastation form input to into the database."""
        
        # form:FlaskForm = UploadForm()
        
        # if form.validate_on_submit():
            
        #     pass
        if request.method == "GET":
            return render_template("add-mediastation.html")
        elif request.method == "POST":
            
            # Errorhandling
            if "msimage" not in request.files or "mssource" not in request.files:
                flash("Es wurden keine Dateien übertragen.")
                return redirect(request.url)
            
            # Mediastation form input values
            ms_name = request.form.get("mstitle", type=str)
            ms_description = request.form.get("msdescription", type=str)
            ms_img = request.files["msimage"]
            ms_path = request.files["mssource"]
            
            # Errorhandling - no input files given
            if ms_img.filename=="" or ms_path.filename=="":
                flash("Es wurde keine Datei ausgewählt")
                return redirect(request.url)
            
            # Extract secure filenames
            fn_img = secure_filename(ms_img.filename)
            fn_path = secure_filename(ms_path.filename)
            
            # Save the files to the corresponding folders
            basedir = os.path.abspath(os.path.dirname(__file__))
            ms_img.save(os.path.join(basedir, app.config["IMG_UPLOAD"], fn_img))
            ms_path.save(os.path.join(basedir, app.config["DATA_UPLOAD"], fn_path))
            
            # Exibition form input values
            ex_name = request.form.get("extitle", type=str)
            ex_location = request.form.get("exlocation", type=str)
            ex_start_date = request.form.get("exsdate", type=str)
            ex_end_date = request.form.get("exedate", type=str)
            ex_description = request.form.get("extrailer", type=str)
                        
            new_ex = Exhibition(title=ex_name, location=ex_location, start_date=ex_start_date, end_date=ex_end_date, trailer=ex_description)
            db.session.add(new_ex)
            db.session.commit()
            
            new_ms = MediaStation(title=ms_name, description=ms_description, image_url=fn_img, path_to_exec=fn_path, exhibition_id=new_ex.id)
            db.session.add(new_ms)
            db.session.commit()
            
            media_types = request.form.getlist("mt")
            interaction_types = request.form.getlist("it")
            visualization_types = request.form.getlist("viz")
            
            media_objects = []
            interaction_objects = []
            visualization_objects = []
            
            for mt in media_types:
                media_objects.append(type_dict["media"][mt])
            
            for it in interaction_types:
                interaction_objects.append(type_dict["interaction"][it])
            
            for viz in visualization_types:
                visualization_objects.append(type_dict["visualization"][viz])
                
            media_content = MediaContent(mediastation_id=new_ms.id)
            
            media_content.media_types.extend(media_objects)
            media_content.interactions.extend(interaction_objects)
            media_content.visualizations.extend(visualization_objects)
            
            db.session.add(media_content)
            db.session.commit()
            
            return render_template("add-mediastation.html")
        
        
    @app.route("/exhibitions")
    def get_exhibitions():
        exhibitions = Exhibition.query.all()
        
        return render_template("exhibitions.html", exhibitions=exhibitions)
    
        """OLD."""
        
        # if not img or path:
        #     return "Keine Bild oder Pfad zur Medienstation angegeben", 400
        
        
    
    
    
    # @app.route("/<id")
    # def user(name):
    #     return str(db.query().all())
    
    # @app.route("/mediastations")
    # def mediastations():
    #     mediastations = db.MediaStation.query.all()
    #     return str(mediastations)
    