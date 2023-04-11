import unittest
from palindromos import palindromo

class TestPalindromos(unittest.TestCase):
    def test_simple(self):
        resultado = palindromo('aba')
        self.assertEqual(resultado, True)
    def test_simple2(self):
        resultado = palindromo('neuquen')
        self.assertEqual(resultado, True)
    def test_simple3(self):
        resultado = palindromo('reinier')
        self.assertEqual(resultado, True)
    def test_simple4(self):
        resultado = palindromo('escuela')
        self.assertEqual(resultado, False)
    def test_simple5(self):
        resultado = palindromo('manzana')
        self.assertEqual(resultado, False)
    def test_simple6(self):
        resultado = palindromo('Neuquen')
        self.assertEqual(resultado, True)

if __name__ == '__main__':
    unittest.main()   