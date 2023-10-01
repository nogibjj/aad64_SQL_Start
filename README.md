# aad64_SQL_Start
Python Scripting, SQL, and Fostering Unified Commitment

[![CI](https://github.com/nogibjj/aad64_SQL_Start/actions/workflows/actions.yml/badge.svg)](https://github.com/nogibjj/aad64_SQL_Start/actions/workflows/actions.yml)

## Requirements
+ Connect to a SQL database:
    For this, extract.py and transform_load.py were created in the mylib folder, which extract the csv dataset from an online github repo, and then establish the connection between my project and SQLite to create the database and a table called Electricity. 

+ Perform CRUD operations and Write at least two different SQL queries:
    Here, the following operations were run:
    * Creation of a database (as previously mentioned)
    * SELECT query to see the first five rows of the database.
    * INSERT to enter a new row to the database. 
    * UPDATE to update the value of a DUPLICATED row created with the INSERT query. 
    * ORDER to order the data as per a particular column in the table.
    * Every time the project is run, a table named Electricity is DELETED.  

* Grading Criteria
    + Database connection (20 points)
    + CRUD operations (20 points)

* Deliverables
    + Python script: [main.py](https://github.com/nogibjj/aad64_SQL_Start/edit/main/main.py). Also check:
        * [extract.py](https://github.com/nogibjj/aad64_SQL_Start/edit/main/mylib/extract.py)
        * [query.py](https://github.com/nogibjj/aad64_SQL_Start/edit/main/mylib/query.py)
        * [transform_load.py](https://github.com/nogibjj/aad64_SQL_Start/edit/main/mylib/transform_load.py)
        * [test_main.py](https://github.com/nogibjj/aad64_SQL_Start/edit/main/test_main.py)
    + Screenshot or log of successful database operations

  Since my test_main.py tests the transform_load.py function as well as all the CRUD operations written in query.py, the following is a screenshot of the successful execution of the test_main.py file (i.e., all the database operation were successful).
+ <img width="1063" alt="Screenshot 2023-10-01 at 6 51 26 PM" src="https://github.com/nogibjj/aad64_SQL_Start/assets/143753050/6fa5152b-f705-4b62-92ce-e2f4e513c906">



