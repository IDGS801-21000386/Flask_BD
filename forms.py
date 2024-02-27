from wtforms import Form, EmailField, validators
from wtforms import StringField, TelField, IntegerField
from flask_wtf import FlaskForm


class UserForm(Form):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message="Ingresa un nombre válido")
    ])
    apaterno = StringField("Apellido Paterno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message="Ingresa un apellido válido")
    ])
    amaterno = StringField("Apellido Materno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=10, message="Ingresa un apellido válido")
    ])
    edad = IntegerField("Edad", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, max=99, message="Ingresa una edad válida")
    ])


class UserForm2(Form):
    id = IntegerField("id", [
        validators.number_range(min=1, max=20, message="El campo es requerido")
    ])
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=20, message="Ingresa un nombre válido")
    ])
    apaterno = StringField("Apellido Paterno", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=4, max=20, message="Ingresa un apellido válido")
    ])
    email = EmailField("correo", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Email(message="Ingrese un correo valido")
    ])


