import sqlite3

connection = sqlite3.connect(":memory:")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE USERS (
        ID INTEGER PRIMARY KEY,
        USERNAME TEXT NOT NULL
    );
""")

cursor.execute("INSERT INTO USERS (ID, USERNAME) VALUES (1, 'Dani')")
cursor.execute("INSERT INTO USERS (ID, USERNAME) VALUES (2, 'Alice')")
cursor.execute("INSERT INTO USERS (ID, USERNAME) VALUES (3, 'Bob')")
user_id = "1 OR 1=1"

query = "SELECT * FROM USERS WHERE ID = ?"

cursor.execute(query, (user_id,))

users = cursor.fetchall()
print(users)