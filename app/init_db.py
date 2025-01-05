import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Connection details
DATABASE_URL = "postgresql://pguser:pwd123@localhost:5432/initial_db"
NEW_DATABASE = "my_database"
NEW_OWNER = "pguser"

# Connect to the initial database
try:
    connection = psycopg2.connect(DATABASE_URL)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)  # Allow database creation
    cursor = connection.cursor()

    # Create a new database
    cursor.execute(f"CREATE DATABASE {NEW_DATABASE} WITH OWNER = {NEW_OWNER};")
    print(f"Database '{NEW_DATABASE}' created with owner '{NEW_OWNER}'.")

    # Close the connection
    cursor.close()
    connection.close()

except Exception as e:
    print(f"Error: {e}")
