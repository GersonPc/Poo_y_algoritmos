import unittest

def suma(num1, num2):
    return num1 +num2

class CajaNegraTest(unittest.TestCase):
    
    def test_suma(self):
        num1 = 10
        num2 = 5

        resultado = suma(num1,num2)

        self.assertEqual(resultado, 15)
    
    def test_suma_negativos(self):
        num1 = -10
        num2 = -5
        resultado = suma(num1, num2)

        self.assertEqual(resultado, -15)

if __name__ == "__main__":
    unittest.main()
