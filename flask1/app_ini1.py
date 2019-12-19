from flask import Flask

#Creamos la instancia
app = Flask(__name__)

@app.route('/')
def index():
    return ("Hola mundo modificadooo ")

# Ejecuto el servidor por default en el pto. 5000
#app.run()
# Especifcando puerto y debug, debug por defaul es False, pero esto no permite estar al escucha de
# los cambios que se realice, debug= True si escuha los cambio que realicemos.
if __name__ == '__main__':
    app.run(debug=True, port=9633)



