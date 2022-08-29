from flask import Flask
from flask import request
from flask import render_template
import sqlite3

class Aplicacion():
    
    def __init__(self, nombre, duda,tabla):
        self.nombre = nombre
        self.duda = duda
        self.tabla = tabla
        self.database = sqlite3.connect('foros.db', check_same_thread=False)
        self.manage_Database = self.database.cursor()
        
    def Insert_Data(self):
        
        Datos_foro = self.nombre, self.duda
        
        self.manage_Database.execute(f'INSERT into {self.tabla}(nombre, duda) VALUES(?, ?)', Datos_foro)
        self.database.commit()
        
    def Extract_Data(self):
        
        self.manage_Database.execute(f'SELECT * FROM {self.tabla}')
        datos = self.manage_Database.fetchall()
        
        return render_template(f'{self.tabla}.html', datos=datos)



server = Flask(__name__)
server.config['SECRET_KEY']= 'tesuo'

@server.route('/')
def Inicio():
    return render_template('foro.html')

@server.route('/comida')
def Comida():
    return render_template('comida.html')

@server.route('/deporte')
def Deporte():
    return render_template('deporte.html')

@server.route('/pelicula')
def Pelicula():
    return render_template('pelicula.html')

@server.route('/tecnologia')
def Tecnologia():
    return render_template('tecnologia.html')

@server.route('/comentario/comida', methods=['POST'])
def comentario_comida():
    nombre = request.form['nombre']
    duda = request.form['duda']
    tabla = 'comida'
    objeto = Aplicacion(nombre, duda, tabla)
    objeto.Insert_Data()
    return objeto.Extract_Data()

@server.route('/comentario/deporte', methods=['POST'])
def comentario_deporte():
    nombre = request.form['nombre']
    duda = request.form['duda']
    tabla = 'deporte'
    objeto = Aplicacion(nombre, duda, tabla)
    objeto.Insert_Data()
    return objeto.Extract_Data()
    
@server.route('/comentario/pelicula', methods=['POST'])
def comentario_pelicula():
    nombre = request.form['nombre']
    duda = request.form['duda']
    tabla = 'pelicula'
    objeto = Aplicacion(nombre, duda, tabla)
    objeto.Insert_Data()
    return objeto.Extract_Data()
    
@server.route('/comentario/tecnologia', methods=['POST'])
def comentario_tecnologia():
    nombre = request.form['nombre']
    duda = request.form['duda']
    tabla = 'tecnologia'
    objeto = Aplicacion(nombre, duda, tabla)
    objeto.Insert_Data()
    return objeto.Extract_Data()
    
if __name__=="__main__":
    server.run(debug=True)