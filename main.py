import sqlite3

db = 'juggle_record_db.sqlite3'

#creating the table if it does not already exist
def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS records (name text, country text, catches int)')
    conn.close()

#inserting the example data given
def insert_example_data():
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO records values("Janne Mustonen", "Finland", 98)')
        conn.execute('INSERT INTO records values("Ian Stewart", "Canada", 94)')
        conn.execute('INSERT INTO records values("Aaron Gregg", "Canada", 88)')
        conn.execute('INSERT INTO records values("Chad Taylor", "USA", 78)')
    conn.close()

#displays all the data in the database
def display_all_data():
    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records')

    for row in results:
        print(row)
    conn.close()

#adds a new record holder ot hte database
def add_new():
    new_name = (input('Please Enter the Name of the record holder: '))
    new_country = (input('Please Enter the country the record holder is from: '))
    new_record = int(input('Please Enter the record: '))

    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO records VALUES(?,?,?)', (new_name, new_country, new_record))
    conn.close()

#searches database for a record holder by record holders name
def search_by_record_holder():
    searched_name = (input('Please enter the name of the record holder you are looking for: '))

    conn = sqlite3.connect(db)
    results = conn.execute('SELECT * FROM records WHERE name = ?', (searched_name, ))

    record_holder = results.fetchone()
    
    if record_holder:
        print(record_holder)
    else:
        print('Record Holder Not Found')
    conn.close()

#updates the catched for an existing record holder, searched db by name
def update_catches():
    updated_name = (input('Please Enter The name of the record holder that you would like to update: '))
    updated_catches = int(input('Please Enter the updated amount of catches: '))

    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE records SET catches = ? WHERE name = ?', (updated_catches, updated_name))
    conn.close()

#deletes an existing record holder by name
def delete_record_holder():
    record_holder_to_be_deleted = (input('Please enter the name of the record holder you would like to delete: '))

    with sqlite3.connect(db) as conn:
        conn.execute('DELETE from records WHERE name = ?', (record_holder_to_be_deleted, ) )
    conn.close()

#prints out a set of options for the user to chose to do with the database
def user_selection():
    
    print(' 1: display all data')
    print(' 2: add a new record')
    print(' 3: search by name of the record holder')
    print(' 4: update existing record')
    print(' 5: delete existing record')

    user_option = int(input('Please select the option you would like to preform: '))
    
    if user_option == 1:
        display_all_data()
    elif user_option == 2:
        add_new()
    elif user_option == 3:
        search_by_record_holder()
    elif user_option == 4:
        update_catches()
    elif user_option == 5:
        delete_record_holder()
    else:
        print('Please enter the number corresponding to the option you would like to select') 

#calls other funcitons
create_table()
insert_example_data()
user_selection()