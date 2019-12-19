from flask import Flask
# Para los parametros
from flask import request

#Creamos la instancia
app = Flask(__name__)

# Ruta http://localhost:9633/
@app.route('/')
def index():
    return "Hola mundo modificadooo "

#Ruta http://localhost:9633/saluda , sin parametro
#Ruta http://localhost:9633/saluda?parametro1=CarlosRubio con parametro
#Ruta http://localhost:9633/saluda?parametro1=CarlosRubio&parametro2=Charly con dos patramtros
@app.route('/saluda')
def saluda():
    param = request.args.get("parametro1", "Es caso de q no mande parametro, es default")
    param2 = request.args.get("parametro2", "Es caso de q no mande parametro2, es default2")
    #return "Es otra ruta "
    return "Es otra ruta con parametro {},{}".format(param,param2)

if __name__ == '__main__':
    app.run(debug=True, port=9633)
