from Modelos.Materia import Materia
class ControladorMateria():
    
    def __init__(self):
        print("Creando ControladorMateria")
    
    def index(self):
        print("Listar tados las materias")
        # unMateria={
        #     "_id":"abc123",
        #     "cedula":"123",
        #     "nombre":"Juan",
        #     "apellido":"Perez"
        # }
        # return [unMateria]
    
    def create(self,infoMateria):
        print("Crear una materia")
        elMateria = Materia(infoMateria)
        return elMateria.__dict__
    
    def show(self,id):
        print("Mostrando una materia con id ",id)
        # elMateria = {
        #     "_id": id,
        #     "cedula": "123",
        #     "nombre": "Juan",
        #     "apellido": "Perez"
        # }
        # return elMateria
    
    def update(self,id,infoMateria):
        print("Actualizando materia con id ",id)
        elMateria = Materia(infoMateria)
        return elMateria.__dict__
    
    def delete(self,id):
        print("Elimiando materia con id ",id)
        return {"deleted_count":1}