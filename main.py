from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

from flask import g
from config import DevelopmentConfig
from forms import UserForm
from  models import db
from  models import Alumnos
import forms 



# Crear una instancia de la clase Flask
app = Flask(__name__)

app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

app.secret_key = "1234"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route("/ABC_Completo", methods=['GET', 'POST'])
def ABC_Completo():
    alum_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    return render_template("ABC_Completo.html", alumno = alumno)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm2(request.form)
    if request.method == "GET":
        id = request.args.get("id")
        # SELECT * FROM alumnos WHERE id = id
        alumn1 = db.session.query(Alumnos).filter(Alumnos.id == id).first
        create_form.id.data = request.args.get("id")
        create_form.nombre.data = alumn1.nombre
        create_form.apaterno.data = alumn1.apaterno
        create_form.email.data = alumn1.email
    if request.method == "POST":
        id = create_form.id.data
        alum = Alumnos.query.get(id)
        # DELETE FROM alumnos WHERE id = id
        db.session.delete(alumn1)
        db.session.commit()
    return render_template("index.html", form = create_form)


@app.route("/index", methods=['GET', 'POST'])
def index():
    create_form = forms.UserForm2(request.form)
    if request.method == "POST":
        alum = Alumnos(nombre = create_form.nombre.data,
                        apaterno = create_form.apaterno.data,
                        email = create_form.email.data
                    )
        db.session.add(alum)
        db.session.commit()
    return render_template("index.html", form = create_form)

#@app.route("/ABC_Completo", methods=['GET', 'POST'])
#def ABC_Completo():
#    create_form = forms.UserForm2(request.form)
#    alumno = Alumno.query.all()


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
    db.init_app(app)

    with app.app_context():
        db.create_all()    
    app.run()
