
# -*- coding: utf8 -*-
from crypt import methods
from flask import Flask
# Importo mi formulario
from flask1 import formulario
#Para redenderizar el html con python, necesitamos la siguiente libreria
from flask import render_template
from flask_wtf import CSRFProtect
# Para las cookies
from flask import make_response,request,session, redirect, url_for

# Para mensajes
from flask import flash


app = Flask(__name__)
# Para proteger la página
app.secret_key = "dfsefFSDASD"
# ES mejor que la clave la tenga una variable de ambiente
app.secret_key = "dfsefFSDASDsdfsdf"
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Al redenderizar le decimos que acepte los metods get y post
@app.route('/')
def index():
    #Obtengo la cookie
    custom_cookie = request.cookies.get('custom_cookie',"Indefinido si no hay valor de cookie")
    print (custom_cookie)
    # Para ver le valor de la variable en sesion
    if 'username' in session:
        username = session['username']
        print (" user.... " , username)

    title = "Index"
    return render_template('index_cookie.html', title=title)

@app.route('/logout')
def logout():
    if 'username' in session:
        # Eliminamos la sesion
        session.pop('username')
    return redirect(url_for('login'))


@app.route('/login', methods = ["GET", "POST"])
def login():
    login_form = formulario.LoginForm(request.form)
    if request.method == "POST" and login_form.validate():
        session ['username'] = login_form.username.data
        username =  login_form.username.data
        success_message = "Bienvenido {}".format(username)
        # Forma correcta de enviar mensajes en flask
        flash(success_message)
    # No es la forma correcta de enviar mensajes
    #return render_template('login.html', form=login_form, message= "Aquí va mí mensaje")
    return render_template('login_mess.html', form=login_form)

@app.route('/cookie')
def cookie():
    response = make_response( render_template('cookie.html') )
    # Instancio ya mis cookies
    response.set_cookie("custom_cookie", "Charly Braum")

    return response

@app.route('/comment', methods = ["GET", "POST"])
def comment():
    pass

# Ejecuto el servidor por default en el pto. 5000
#app.run()
# Especifcando puerto y debug, debug por defaul es False, pero esto no permite estar al escucha de
# los cambios que se realice, debug= True si escucha los cambio que realicemos.
if __name__ == '__main__':
    app.run(debug=True, port=9333)
