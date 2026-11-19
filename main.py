import csv #lingocon interop
import sqlite3 #complex queries and rollbacks

def check_if_db_exists(wipe_and_reload):

    # Connect to Database
    with sqlite3.connect("dict.db") as conn:
        cursor = conn.cursor()

        
        if wipe_and_reload: # If the toggle is True, completely nuke the old table first
            cursor.execute("DROP TABLE IF EXISTS dictionary;")
            print("Wiped existing database table.")

        # Check if the table exists, if not create it
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS dictionary (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                lemma TEXT NOT NULL,
                gloss TEXT NOT NULL,
                ipa TEXT,
                part_of_speech TEXT,
                etymology TEXT,
                notes TEXT,
                tags TEXT,
                related_words TEXT
            )
            '''
            )

def load_csv_to_db():
    rows_to_insert = [] # csv contents to write to table

    with open("MOPX-dict.csv", "r", encoding="utf-8") as file:
        data = csv.DictReader(file) #csv.DictReader reads the CSV file and returns each row as a dictionary, where the keys are the column headers and the values are the corresponding data for that row.

        for row in data:
            rows_to_insert.append((
                row.get("Lemma"),
                row.get("Gloss"),
                row.get("IPA") or None, # or None correctly inserts NULL values into the database for empty fields
                row.get("Part of Speech") or None,
                row.get("Etymology") or None,
                row.get("Notes") or None,
                row.get("Tags") or None,
                row.get("Related Words") or None,
        ))

    # Connect to Database
    with sqlite3.connect("dict.db") as conn:
        cursor = conn.cursor()

        # Insert data into the table
        cursor.executemany( # executemany is used to insert multiple rows into the database in a single operation, which is more efficient than inserting them one by one.
            '''
            INSERT INTO dictionary (lemma, gloss, ipa, part_of_speech, etymology, notes, tags, related_words)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?) 
            ''', # using parameterized queries (the ? placeholders) helps prevent SQL injection attacks and ensures that the data is properly escaped.
            rows_to_insert #this is where we are passing the actually data to be inserted into the database. The rows_to_insert list contains tuples of values corresponding to each row in the CSV file.
        )

    print(
        f"Successfully imported {len(rows_to_insert)} rows into the database!"
    )

def verify_db_contents_with_limit(limit):
    with sqlite3.connect("dict.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM dictionary LIMIT ?;", (limit,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)

def verify_db_contents_by_count():
    with sqlite3.connect("dict.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM dictionary;")
        total_rows = cursor.fetchone()[0]
        print(f"Total rows in database: {total_rows}")

if __name__ == "__main__":

    '''
    Basically, "wipe_and_reload" is a toggle that allows you to choose whether to completely wipe the existing database and reload it from the CSV file or just check if the database exists and create it if it doesn't. If you set "wipe_and_reload" to True, it will drop the existing table (if it exists) and then load the data from the CSV file into a new table. If you set it to False, it will only check if the table exists and create it if necessary, without modifying any existing data.
    '''
    wipe_and_reload = False # Set to True if you want to wipe the database and reload it from the CSV file
    check_if_db_exists(wipe_and_reload)
    if wipe_and_reload:
        load_csv_to_db()
        #verify_db_contents_with_limit(5) # Uncomment this line to verify the first 5 rows of the database
        verify_db_contents_by_count()
