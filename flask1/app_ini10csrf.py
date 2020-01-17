#
# -*- coding: utf8 -*-
from crypt import methods
from flask import Flask
# Importo mi formulario
from flask1 import formulario
#Para redenderizar el html con python, necesitamos la siguiente libreria
from flask import render_template
from flask import request
import wtforms

from flask_wtf import CSRFProtect




app = Flask(__name__)
# Para proteger la página
app.secret_key = "dfsefFSDASD"
# ES mejor que la clave la tenga una variable de ambiente
app.secret_key = "dfsefFSDASDsdfsdf"
csrf = CSRFProtect(app)


# Al redenderizar le decimos que acepte los metods get y post
@app.route('/')
def index():
    pass

@app.route('/login', methods = ["GET", "POST"])
def login():
    login_form = formulario.LoginForm()
    return render_template('login.html', form=login_form)

@app.route('/cookie')
def cookie():
    return render_template('cookie.html')

@app.route('/comment', methods = ["GET", "POST"])
def comment():


    """
# Al redenderizar le decimos que acepte los metods get y post
@app.route('/', methods = ["GET", "POST"])
def index():
    # Instancio mi formulario
    comment_form = formulario.CommentForm(request.form)
                                    # Para que ejecute las validadiones
    if request.method == "POST" and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print("Error en el formulario!!!")

    titulo = "Curso Flask"
    return render_template('index_formulario.html', title = titulo, form=comment_form)
    """

# Ejecuto el servidor por default en el pto. 5000
#app.run()
# Especifcando puerto y debug, debug por defaul es False, pero esto no permite estar al escucha de
# los cambios que se realice, debug= True si escucha los cambio que realicemos.
if __name__ == '__main__':
    app.run(debug=True, port=9333)
