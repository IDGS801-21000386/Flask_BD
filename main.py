from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
import forms 


# Crear una instancia de la clase Flask
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

app.secret_key = "1234"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods={"GET", "POST"})
def alumnos():
    nom=""
    apa=""
    ama=""
    edad=""
    #email=""
    alumno_clase = forms.UserForm(request.form)
    if request.method == "POST" and alumno_clase.validate():
        nom = alumno_clase.nombre.data
        apa = alumno_clase.apaterno.data
        ama = alumno_clase.amaterno.data
        edad = alumno_clase.edad.data
        #email = alumno_clase.email.data
        print(f'Nombre: {nom}')
        print(f'Apellido paterno: {apa}')
        print(f'Apellido materno: {ama}')
        print(f'Edad: {edad}')


        mensaje = f"Bienvenido {nom}"
        flash(mensaje)

    return render_template("alumnos2.html", form = alumno_clase, nom=nom, apa=apa, ama=ama, edad=edad)

    
if __name__ == "__main__":
    csrf.init_app(app)
    
    app.run()
