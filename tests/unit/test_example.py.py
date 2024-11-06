import unittest
from app import main
from io import StringIO
import sys

class TestApp(unittest.TestCase):
    def test_main_output(self):
        # Redirigir la salida estándar a un StringIO para capturar el output de la función main
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Llamar a la función main
        main()
        
        # Restaurar la salida estándar y comparar el resultado
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hola, Mundo")

if __name__ == '__main__':
    unittest.main()