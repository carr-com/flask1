#
# -*- coding: utf8 -*-
from flask import Flask

#Para redenderizar el html con python, necesitamos la siguiente libreria
from flask import render_template

#Creamos la instancia
app = Flask(__name__)

@app.route('/user/')
@app.route('/user/<name>')
def user(name="Sin nombre como parametro"):
    age = 18
    my_list = [1,2,3,4,5,6]
    # Template a redenderizar, los archivos .html deben d eestar en el directorio llamados templates,
    # no template sin la s por que marca error.
    return render_template('user.html', nombre=name, edad = age, lista = my_list)

# Ejecuto el servidor por default en el pto. 5000
#app.run()
# Especifcando puerto y debug, debug por defaul es False, pero esto no permite estar al escucha de
# los cambios que se realice, debug= True si escucha los cambio que realicemos.
if __name__ == '__main__':
    app.run(debug=True, port=9333)
