#
# -*- coding: utf8 -*-
from flask import Flask

#Para redenderizar el html con python, necesitamos la siguiente libreria
from flask import render_template

#Creamos la instancia
#app = Flask(__name__)
#Creamos la instancia  cambiando el nombre del folder  templates por defaul a vistas.
app = Flask(__name__, template_folder='vistas')
# Ahpra buscara el archivo index.html en el folder vistas

@app.route('/')
def index():
    # Template a redenderizar, los archivos .html deben d eestar en el directorio llamados templates,
    # no template sin la s por que marca error. Si queremos que esta carpeta lleve ostro nombre lo
    # debemos de indicar en la creacion de la instancia.
    return render_template('index.html')

# Ejecuto el servidor por default en el pto. 5000
#app.run()
# Especifcando puerto y debug, debug por defaul es False, pero esto no permite estar al escucha de
# los cambios que se realice, debug= True si escucha los cambio que realicemos.
if __name__ == '__main__':
    app.run(debug=True, port=9333)
