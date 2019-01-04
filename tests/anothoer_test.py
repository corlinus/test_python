import unittest
from another import Another

class TestSmthAddToValue(unittest.TestCase):
    def test_value(self):
        subject = Another()
        self.assertEqual(subject.value, 10)
