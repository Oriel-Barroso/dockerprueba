from persona import Persona

class Service:
    def add_person(self, nombre, apellido, edad):
        return Persona(nombre, apellido, edad).__dict__

    def check_age(self, edad):
        if edad < 18:
            return ('Es menor de edad')
        elif edad > 18:
            return ('Es mayor de edad')
        

if __name__ == '__main__':
    persona = Persona()
    serv = Service()
    persona = serv.add_person('Oriel', 'Barroso', 24)
    print(persona)
    edad = serv.check_age(persona['_edad'])
    print(edad)

