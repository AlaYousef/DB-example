import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = psycopg2.cursor()

results = cursor.fetchall()

connection.close()

for result in results:
    print(result)
