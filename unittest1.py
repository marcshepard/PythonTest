"""unit test for pytest"""
import unittest
import pythontest

class PythontestTests(unittest.TestCase):
    """unit tests for pytest"""
    def setUp(self):
        """Run before each test"""

    def tearDown(self):
        """Run after each test"""

    def test_pyprint(self):
        """"test for pyprint"""
        arg = "a test argument"
        self.assertEqual(arg, pythontest.pyprint(arg))

    def test_noop(self):
        """"dummy test method"""

if __name__ == '__main__':
    unittest.main()
