#
# -*- coding: utf8 -*-
from flask import Flask

#Para redenderizar el html con python, necesitamos la siguiente libreria
from flask import render_template

#Creamos la instancia
app = Flask(__name__)

@app.route('/')
def user(name="Sin nombre como parametro"):
    return render_template('index_extends.html', nombre=name)

@app.route('/client')
def cliente():
    list_cte = ['cte1','cte2','cte3']
    return render_template('client.html', l_ctes=list_cte)


if __name__ == '__main__':
    app.run(debug=True, port=9333)
