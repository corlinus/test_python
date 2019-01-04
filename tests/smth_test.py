import unittest

import sys
from smth import Smth
from another import Another

class TestSmthAddToValue(unittest.TestCase):
    def test_returns_new_value(self):
        subject = Smth()
        self.assertEqual(subject.add_to_value(10), 20)

    def test_changes_value(self):
        subject = Smth()
        subject.add_to_value(10)
        self.assertEqual(subject.value, 20)
