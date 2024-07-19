# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileRequired, FileAllowed
# from wtforms import SubmitField
# from app import ms_images, ms_data

# class UploadForm(FlaskForm):
#     image = FileField(
#         validators=[
#             FileAllowed(ms_images, "Es dürfen nur Bilder verwendet werden."),
#             FileRequired("Das Datei-Upload Formfeld darf nicht leer sein.")
#         ]
        
#     )
#     submit = SubmitField("Submit")