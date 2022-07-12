from flask import Flask
from flask_mysqldb import MySQL

from config import config

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/')
def listar_cursos():
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso"
        cursor.execute(sql)
        datos=cursor.fetchall()
        print(datos)
        return "Cursos listados!"
    except Exception as ex:
        return "Error"

def pagina_no_encontrada(error):
    return "<h1>La página que intentas buscar no existe ...</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])    
    app.register_error_handler(404, pagina_no_encontrada) 
    app.run()
    
    
