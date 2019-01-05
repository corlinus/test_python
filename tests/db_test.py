import unittest
import os
from db import DB

class TestDB(unittest.TestCase):
    def test_class(self):
        self.assertIsInstance(self.subject(), DB)

    def test_file_name(self):
        self.assertTrue(str.endswith(self.subject().file_name(), 'db/test.db'))

    def execute_and_fetch():
        query = "SELECT name FROM sqlite_master WHERE name='some_table'"
        self.assertEqual(self.subject().execute_and_fetch(query), [])

    def subject(self):
        return DB()
