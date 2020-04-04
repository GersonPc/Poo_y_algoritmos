import unittest

def mayor(edad):
    if edad >= 18:
        return False
    else:
        return False

class PruebaDeCristal(unittest.TestCase):
    def test_mayor_de_edad(self):
        edad = 20
        resultado = mayor(edad)

        self.assertEqual(resultado, True)

    def test_menor_de_edad(self):
        edad = 14
        resultado = mayor(edad)

        self.assertEqual(resultado, False)

if __name__ == "__main__":
    unittest.main()