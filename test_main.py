import unittest
import sqlite3
from mylib.query import see_five_query, insert_query, update_query, order_query
from mylib.transform_load import load


class TestElectricityFunctionsPartOne(unittest.TestCase):
    def test_load_function(self):
        """TESTING THE CREATION OF A DATABASE, i.e., testing transform_load.py"""
        db_file = load("test_dataset.csv")
        self.assertTrue(db_file == "Electricity.db")
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='Electricity';"
        )
        table_exists = cursor.fetchone()
        self.assertIsNotNone(table_exists)
        cursor.execute("SELECT COUNT(*) FROM Electricity;")
        row_count = cursor.fetchone()[0]
        self.assertEqual(row_count, 37792)
        conn.close()

    def test_see_five_query(self):
        """Testing is the size of the see_fice_query output is 5, 9"""
        result = see_five_query()
        num_rows = len(result)
        num_columns = len(result[0])
        self.assertEqual(num_rows, 5)
        self.assertEqual(num_columns, 9)

    def test_insert_query(self):
        """Testing INSERT query"""
        conn = sqlite3.connect("Electricity.db")
        cursor = conn.cursor()
        insert_query()
        cursor.execute(
            """
            SELECT zip FROM Electricity WHERE 
            utility_name = 'Data Engineering Electric';
            """
        )
        result = cursor.fetchone()
        self.assertEqual(result[0], 55555)
        conn.close()

    def test_update_query(self):
        """Testing UPDATE query"""
        conn = sqlite3.connect("Electricity.db")
        cursor = conn.cursor()
        update_query()
        cursor.execute("SELECT zip FROM Electricity WHERE eiaid = 000;")
        result = cursor.fetchone()
        self.assertEqual(result[0], 55501)
        conn.close()

    def test_order_query(self):
        """Testing ORDER query"""
        conn = sqlite3.connect("Electricity.db")
        cursor = conn.cursor()
        order_query()
        cursor.execute("SELECT * FROM Electricity;")
        result = cursor.fetchall()
        self.assertTrue(result[0][-7] >= result[1][-7])
        conn.close()


if __name__ == "__main__":
    unittest.main()
