import unittest
import sys
from io import StringIO
from main import add_meter, verify_meter, display_meters, home

class TestMeterVerificationApp(unittest.TestCase):

    def setUp(self):
        self.app_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.app_output

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_add_meter(self):
        meters = {}
        add_meter('Лічильник1', meters)
        output = self.app_output.getvalue().strip()
        self.assertIn('Лічильник1  успішно додано.', output)

    def test_verify_meter(self):
        meters = {}
        add_meter('Лічильник2', meters)
        verify_meter('Лічильник2', meters)
        output = self.app_output.getvalue().strip()
        self.assertIn('Лічильник2 підтверджено.', output)

    def test_invalid_verify_meter(self):
        meters = {}
        with self.assertRaises(KeyError):
            verify_meter('Не існуючий лічильник', meters)

    def test_home_route(self):
        response = home().strip()
        self.assertIn('Лічильник1: Підтверджено', response)
        self.assertIn('Лічильник2: Не підтверджено', response)

if __name__ == "__main__":
    unittest.main()
