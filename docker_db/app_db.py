import psycopg2

print('hello world before')

conn = psycopg2.connect(dbname="stage", user="postgres", password="secret", host="db", port="5432")
cursor = conn.cursor()

cursor.execute("INSERT into test (first_name, second_name) VALUES ('Ivan', 'Ivanov');")
conn.commit()

print('hello world after')
