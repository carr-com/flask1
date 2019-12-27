#
# -*- coding: utf8 -*-
from flask import Flask

#Para redenderizar el html con python, necesitamos la siguiente libreria
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_static.html')

# Ejecuto el servidor por default en el pto. 5000
#app.run()
# Especifcando puerto y debug, debug por defaul es False, pero esto no permite estar al escucha de
# los cambios que se realice, debug= True si escucha los cambio que realicemos.
if __name__ == '__main__':
    app.run(debug=True, port=9333)
