import unittest
def palindromo(palabra):
    palabra1 = palabra.lower()
    lista = list(palabra1)
    alreves = []
    total = 1
    for i in lista:
        alreves += lista[-total]
        total += 1 
    if lista == alreves:
        return True
    else:
        return False
    
if __name__ == '__main__':
    unittest.main()