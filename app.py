import json
from http import client

import certifi
import pymongo
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from waitress import serve

app=Flask(__name__)
cors = CORS(app)

from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorInscripcion import ControladorInscripcion
from Controladores.ControladorMateria import ControladorMateria

miControladorEstudiante=ControladorEstudiante()
miControladorDepartamento=ControladorDepartamento()
miControladorMateria=ControladorMateria()
miControladorInscripcion=ControladorInscripcion()

def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)

@app.route("/estudiantes",methods=['GET'])
def getEstudiantes():
    json=miControladorEstudiante.index()
    return jsonify(json)

@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json=miControladorEstudiante.create(data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    json=miControladorEstudiante.show(id)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json=miControladorEstudiante.update(id,data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json=miControladorEstudiante.delete(id)
    return jsonify(json)

@app.route("/departamentos",methods=['GET'])
def getDepartamentos():
    json=miControladorDepartamento.index()
    return jsonify(json)

@app.route("/departamentos",methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    json=miControladorDepartamento.create(data)
    return jsonify(json)

@app.route("/departamentos/<string:id>",methods=['GET'])
def getDepartamento(id):
    json=miControladorDepartamento.show(id)
    return jsonify(json)

@app.route("/departamentos/<string:id>",methods=['PUT'])
def modificarDepartamento(id):
    data = request.get_json()
    json=miControladorDepartamento.update(id,data)
    return jsonify(json)

@app.route("/departamentos/<string:id>",methods=['DELETE'])
def eliminarDepartamento(id):
    json=miControladorDepartamento.delete(id)
    return jsonify(json)

@app.route("/materias",methods=['GET'])
def getMaterias():
    json=miControladorMateria.index()
    return jsonify(json)

@app.route("/materias",methods=['POST'])
def crearMateria():
    data = request.get_json()
    json=miControladorMateria.create(data)
    return jsonify(json)

@app.route("/materias/<string:id>",methods=['GET'])
def getMateria(id):
    json=miControladorMateria.show(id)
    return jsonify(json)

@app.route("/materias/<string:id>",methods=['PUT'])
def modificarMateria(id):
    data = request.get_json()
    json=miControladorMateria.update(id,data)
    return jsonify(json)

@app.route("/materias/<string:id>",methods=['DELETE'])
def eliminarMateria(id):
    json=miControladorMateria.delete(id)
    return jsonify(json)

@app.route("/inscripciones",methods=['GET'])
def getInscripciones():
    json=miControladorInscripcion.index()
    return jsonify(json)

@app.route("/inscripciones/<string:id>",methods=['GET'])
def getInscripcion(id):
    json=miControladorInscripcion.show(id)
    return jsonify(json)

@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.create(data,id_estudiante,id_materia)
    return jsonify(json)

@app.route("/inscripciones/<string:id_inscripcion>/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['PUT'])
def modificarInscripcion(id_inscripcion,id_estudiante,id_materia):
    data = request.get_json()
    json=miControladorInscripcion.update(id_inscripcion,data,id_estudiante,id_materia)
    return jsonify(json)

@app.route("/inscripciones/<string:id_inscripcion>",methods=['DELETE'])
def eliminarInscripcion(id_inscripcion):
    json=miControladorInscripcion.delete(id_inscripcion)
    return jsonify(json)

@app.route("/materias/<string:id>/departamento/<string:id_departamento>",methods=['PUT'])
def asignarDepartamentoAMateria(id,id_departamento):
    json=miControladorMateria.asignarDepartamento(id,id_departamento)
    return jsonify(json)

if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])
    # ca= certifi.where()
    # client = pymongo.MongoClient(dataConfig["data-db-connection"],tlsCAFile=ca)
    # baseDatos=client[dataConfig["name-db"]]
    # print(baseDatos.list_collection_names())
