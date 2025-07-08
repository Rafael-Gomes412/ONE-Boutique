from django.db import connection
from django.test import TestCase

class DatabaseConnectionTest(TestCase):
    def test_connection_is_available(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            self.assertEqual(result[0], 1)