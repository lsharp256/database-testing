# This test uses a fixture to establish a connection to the psql database, 
# which is then passed to the two test functions as an argument. 
# The first test function verifies that the connection to the database is open, 
# while the second test function runs a query on the database and verifies that 
# the query returns at least one row of data.
import pytest
import psycopg2

@pytest.fixture(scope="session")
def psql_database():
    # Establish a connection to the psql database
    conn = psycopg2.connect(
        host="localhost",
        database="testdb",
        user="testuser",
        password="testpassword"
    )
    yield conn
    # Close the connection to the database
    conn.close()

def test_psql_connection(psql_database):
    # Test that we can connect to the psql database
    assert psql_database.closed == False

def test_psql_query(psql_database):
    # Test that we can run a query on the psql database
    cur = psql_database.cursor()
    cur.execute("SELECT * FROM test_table")
    rows = cur.fetchall()
    assert len(rows) > 0
