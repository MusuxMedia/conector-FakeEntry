import unittest

from src.DisplayParser import DisplayParser
from fastapi import HTTPException


class DisplayParserTest(unittest.TestCase):

    def test_lista_feliz(self):
        lista_correcta = [1, 2, 3]
        lista_a_testear = "[1,2,3]"
        self.assertEqual(DisplayParser().parse(lista_a_testear), lista_correcta)

    def test_lista_negativos_y_ceros(self):
        lista_correcta = [0, -1, -100]
        lista_a_testear = "[0, -1, -100]"
        self.assertEqual(DisplayParser().parse(lista_a_testear), lista_correcta)

    def test_valor_vacio(self):
        lista_a_testear = ""
        with self.assertRaises(HTTPException):
            DisplayParser().parse(lista_a_testear)

    def test_display_no_numero(self):
        lista_a_testear = "[a]"
        with self.assertRaises(HTTPException):
            DisplayParser().parse(lista_a_testear)

    def test_lista_vacia(self):
        lista_a_testear = "[]"
        with self.assertRaises(HTTPException):
            DisplayParser().parse(lista_a_testear)


if __name__ == '__main__':
    unittest.main()
