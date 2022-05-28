import psycopg2

print('hello world before')

conn = psycopg2.connect(database="stage", user="postgres", password="secret", host="127.0.0.1", port="5460")
cursor = conn.cursor()

cursor.execute("CREATE TABLE hello_world (hello TEXT, world TEXT);")

print('hello world after')
