import unittest
#from main import sumar

def sumar(a,b):
    return a+b


class MyTestCase(unittest.TestCase):
    def test_sumando2y2_resultado4(self):
        resultado = sumar(2,2)
        self.assertEqual(resultado, 4)

    def test_sumando2y3_resultado4(self):
        self.assertNotEqual(sumar(2,3), 4)

if __name__ == '__main__':
    unittest.main()