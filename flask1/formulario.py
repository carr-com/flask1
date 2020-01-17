from wtforms import Form
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField

#Para validar los campos del formulario
from wtforms  import validators
# Para ocultar campos
from wtforms import HiddenField

# Función ṕara validación propia
def length_honeypot(form,field):
    if len(field.data) >  0:
        raise validators.ValidationError("El campo debe estar vacio!!")


class CommentForm(Form):
    username = StringField("Usuario",
                           [    # Las validaciones se ejecutan en orden
                                validators.DataRequired("El usuario es requerido!!"),
                                validators.length(min=4, max=25, message="Ingrese un usuario válido")
                           ]
                           )
    email = EmailField("Correo Electrónico",
                            [
                                validators.DataRequired("El Email es requerido!!"),
                                validators.Email(message="Ingrese un Email válido!!")

                            ]
                       )
    comment = TextAreaField("Comentario")
    """ MOstramos el campo para ejemplo pero al final va oculto
    #Campo para ejemplificar validaciones propias
    honeypot = StringField("", #No lleva etiqueta por que será oculto
                           [
                               length_honeypot #Validacion propia hecha con una función
                            ]
                           )
    """
    #Campo para ejemplificar validaciones propias
    honeypot = HiddenField("", #No lleva etiqueta por que será oculto
                           [
                               length_honeypot #Validacion propia hecha con una función
                            ]
                           )

class LoginForm(Form):

    username = StringField("Usuario",
                           [    # Las validaciones se ejecutan en orden
                                validators.DataRequired("El usuario es requerido!!"),
                                validators.length(min=4, max=25, message="Ingrese un usuario válido")
                           ]
                           )
    password = PasswordField("Password",
                            [
                                validators.DataRequired("El password es requerido!!")
                            ]
                       )

    #Campo para ejemplificar validaciones propias
    honeypot = HiddenField("", #No lleva etiqueta por que será oculto
                           [
                               length_honeypot #Validacion propia hecha con una función
                            ]
                           )
