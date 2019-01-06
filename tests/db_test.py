import unittest
import os
from db import DB

class TestDB(unittest.TestCase):
    def test_class(self):
        self.assertIsInstance(self.subject(), DB)

    def test_file_name(self):
        self.assertTrue(str.endswith(
            self.subject().file_name(),
            os.path.join('db', 'test.db'))
        )

    def test_execute_and_fetch(self):
        query = "SELECT name FROM sqlite_master WHERE name='some_table'"
        self.assertEqual(self.subject().execute_and_fetch(query), [])

    def test_execute_and_fetch_with_args(self):
        query = "SELECT name FROM sqlite_master WHERE name=?"
        self.assertEqual(self.subject().execute_and_fetch(query, "some_table"), [])

    def subject(self):
        return DB()
