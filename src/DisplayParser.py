from ast import literal_eval

from src.tests.BusinessException import BusinessException


class DisplayParser:

    def parse(self, pantallas: str):
        try:
            return literal_eval(pantallas)
        except SyntaxError:
            raise BusinessException("Display incorrecto, recordar utilizar [] y separar los valores por coma")
        except ValueError:
            raise BusinessException("Display incorrecto, el valor debe ser un numero")
