from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Alumnos(db.Model):
    __tablename__ = "alumnos" # Establece el nombre de la tabla
    id = db.Column(db.Integer, primary_key = True) # Es necesario SIEMPRE el campo id para fungir como pk
    nombre = db.Column(db.String(50)) # Se establece el tipo de columna que se generara
    apaterno = db.Column(db.String(50))
    email = db.Column(db.String(50))
    create_date = db.Column(db.DateTime, default = datetime.datetime.now)

