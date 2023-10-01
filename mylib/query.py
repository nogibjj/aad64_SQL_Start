"""Query the database"""

import sqlite3


def see_five_query():
    """Query the database for the top 5 rows of the ElectricityDB table"""
    conn = sqlite3.connect("Electricity.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Electricity")
    print("Top 5 rows of the Electricity table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


def insert_query():
    """Query the Database to add a row with Electricity information."""
    conn = sqlite3.connect("Electricity.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Electricity 
        (zip, eiaid, utility_name, state, service_type, ownership, comm_rate, ind_rate, res_rate) 
        VALUES 
        (55555, 555, "Data Engineering Electric", "NC", "Artificial", "Self Owned", 0.555, 0.12345, 0.75000);
    """
    )
    conn.commit()
    conn.close()


def update_query():
    """Query the database to update recently added row"""
    conn = sqlite3.connect("Electricity.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Electricity 
        (zip, eiaid, utility_name, state, service_type, ownership, comm_rate, ind_rate, res_rate) 
        VALUES (55500, 000, "ABC", "NY", "Home", "Private", 0.500, 0.750, 1.500);
        """
    )
    cursor.execute("UPDATE Electricity SET zip = 55501 WHERE eiaid = 000;")
    conn.commit()
    conn.close()


def order_query():
    """Query the database to reorder the database to be in descending order of individual rate"""
    conn = sqlite3.connect("Electricity.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Electricity ORDER BY ind_rate DESC;")
    conn.commit()
    conn.close()
