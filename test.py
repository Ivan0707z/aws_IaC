import unittest
import sys
import main
from io import StringIO

class TestMeterVerificationApp(unittest.TestCase):

    def setUp(self):
        self.app_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.app_output

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_add_meter(self):
        meters = {}
        main.add_meter('Лічильник1', meters)
        main.display_meters(meters)
        output = self.app_output.getvalue().strip()
        self.assertIn('Лічильник1: Не підтверджено', output)

    def test_verify_meter(self):
        meters = {}
        main.add_meter('Лічильник2', meters)
        main.verify_meter('Лічильник2', meters)
        main.display_meters(meters)
        output = self.app_output.getvalue().strip()
        self.assertIn('Лічильник2: Підтверджено', output)

    def test_invalid_verify_meter(self):
        meters = {}
        with self.assertRaises(KeyError):
            main.verify_meter('Не існуючий лічильник', meters)

    def test_display_meters(self):
        meters = {}
        main.add_meter('Лічильник3', meters)
        main.add_meter('Лічильник4', meters)
        main.display_meters(meters)
        output = self.app_output.getvalue().strip()
        self.assertIn('Лічильник3: Не підтверджено', output)
        self.assertIn('Лічильник4: Не підтверджено', output)

if __name__ == "__main__":

    unittest.main()
