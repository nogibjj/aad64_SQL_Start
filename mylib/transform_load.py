"""
Transforms and Loads data into the local SQLite3 database
Example:
zip,eiaid,utility_name,state,service_type,ownership,comm_rate,ind_rate,res_rate
"""
import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(
    dataset="Electricity.csv",
):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("Electricity.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS Electricity")
    c.execute(
        "CREATE TABLE Electricity (zip,eiaid,utility_name,state,service_type,ownership,comm_rate,ind_rate,res_rate)"
    )
    # insert
    c.executemany("INSERT INTO Electricity VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "Electricity.db"
