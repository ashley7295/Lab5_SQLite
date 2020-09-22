import sqlite3

db = 'juggle_record_db.sqlite3'

def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS records (name text, country text, catches int)')
    conn.close()

def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO records values("Janne Mustonen", "Finland", 98)')
        conn.execute('INSERT INTO records values("Ian Stewart", "Canada", 94)')
        conn.execute('INSERT INTO records values("Aaron Gregg", "Canada", 88)')
        conn.execute('INSERT INTO records values("Chad Taylor", "USA", 78)')
    conn.close()


        














create_table()
insert_example_data()
add_new()
search_by_record_holder()
Update_catches()
delete_record_holder()