from flask import Flask
# Para los parametros
from flask import request

#Creamos la instancia
app = Flask(__name__)

# Ruta http://localhost:9633/
@app.route('/')
def index():
    return "Hola mundo modificadooo "


# Otra forma de parametros
@app.route('/saluda/') # Si no manda paramtros, para que no de error
@app.route('/saluda/<name>/')
@app.route('/saluda/<name>/<apellido>/')
#http://localhost:9633/saluda/Carlos/Rubio/
@app.route('/saluda/<name>/<apellido>/<int:num>/')
# int: valida que la entrada se aun numero
def saluda(name= "Valor por defaul por si no manda parametros y no de error", apellido="ninguno",num=0):
    #return "Es otra ruta "
    return "Es otra ruta con parametro {} {} {}".format(name,apellido,num)

if __name__ == '__main__':
    app.run(debug=True, port=9633)
