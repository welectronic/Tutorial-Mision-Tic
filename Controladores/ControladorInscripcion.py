from Modelos.Inscripcion import Inscripcion
class ControladorInscripcion():
    
    def __init__(self):
        print("Creando ControladorInscripcion")
    
    def index(self):
        print("Listar todas las inscripciones")
        # unInscripcion={
        #     "_id":"abc123",
        #     "cedula":"123",
        #     "nombre":"Juan",
        #     "apellido":"Perez"
        # }
        # return [unInscripcion]
    
    def create(self,infoInscripcion):
        print("Crear un inscripción")
        elInscripcion = Inscripcion(infoInscripcion)
        return elInscripcion.__dict__
    
    def show(self,id):
        print("Mostrando un inscripción con id ",id)
        # elInscripcion = {
        #     "_id": id,
        #     "cedula": "123",
        #     "nombre": "Juan",
        #     "apellido": "Perez"
        # }
        # return elInscripcion
    
    def update(self,id,infoInscripcion):
        print("Actualizando inscripción con id ",id)
        elInscripcion = Inscripcion(infoInscripcion)
        return elInscripcion.__dict__
    
    def delete(self,id):
        print("Elimiando inscripción con id ",id)
        return {"deleted_count":1}