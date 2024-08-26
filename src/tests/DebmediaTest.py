import unittest

from src.Demedia import Debmedia


class DebmTest(unittest.TestCase):
    def test_fake_entry(self):
        consulta = Debmedia().fake_entry(consultorio="hola", paciente="<NAME>", token="29082eb96c01453b9917a6b7e326e8bd",
                              pantallas=[3166])
        self.assertEqual(consulta, 200)


if __name__ == '__main__':
    unittest.main()
