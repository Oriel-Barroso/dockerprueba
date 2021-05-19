class Persona:
    def __init__(self, nombre=None, apellido=None, edad=0):
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
    
    def __str__(self):
        return (f'El nombre es {self.nombre}, y su apellido {self.apellido}')

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor
    
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = int(valor)

