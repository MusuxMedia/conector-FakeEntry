import unittest

from src.Demedia import Debmedia
from fastapi import HTTPException


class DebmTest(unittest.TestCase):
    def test_fake_entry(self):
        consulta = Debmedia().fake_entry(consultorio="a", turno="<NAME>", token="29082eb96c01453b9917a6b7e326e8bd",
                                         pantallas=[566])
        self.assertEqual(consulta, 200)

    def test_token(self):
        with self.assertRaises(HTTPException):
            Debmedia().fake_entry(consultorio="a", turno="<NAME>", token="1111111111111",
                                  pantallas=[566])


if __name__ == '__main__':
    unittest.main()
