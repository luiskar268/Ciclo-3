from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class FormInicio(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacío,  completar')])
    contrasena = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacío, completar')])
    recordar = BooleanField('Recordar Usuario')
    enviar = SubmitField('Iniciar Sesión')

    def validate_on_submit(self)->bool:
        return False