import unittest
from persona import Persona
from service import Service


class TestPersona(unittest.TestCase):
    def test_constructor_con_valores_iniciales_partida(self):
        persona = Persona()
        serv = Service()
        persona = serv.add_person('Oriel', 'Barroso', 24)
        self.assertEqual(persona, {'_nombre': 'Oriel',
                                   '_apellido': 'Barroso',
                                   '_edad': 24})
    
    def test_edad(self):
        serv = Service()
        edad = serv.check_age(24)
        self.assertEqual(edad, 'Es mayor de edad')
    

if __name__ == '__main__':
    unittest.main()