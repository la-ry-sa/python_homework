import sqlite3

try:
# Connect to a new SQLite database
    with  sqlite3.connect("db/magazines.db") as conn:  
        print("Database created and connected successfully.")

except sqlite3.Error as e:
     print(f"An error occurred: {e}")

with sqlite3.connect("db/magazines.db") as conn:
    cursor = conn.cursor()
    conn.execute("PRAGMA foreign_keys = 1")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS publishers (
        publisher_id INTEGER PRIMARY KEY,
        publisher_name TEXT NOT NULL UNIQUE
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        magazine_id INTEGER PRIMARY KEY,
        magazine_name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES publishers (publisher_id)
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        subscriber_name TEXT NOT NULL,
        subscriber_address TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        expiration_date DATE NOT NULL,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        FOREIGN KEY (subscriber_id) REFERENCES subscribers (subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES magazines (magazine_id)
    )
    """)

    def add_publisher(cursor, name):
        try:
            cursor.execute("INSERT INTO publishers (publisher_name) VALUES (?)", (name,))
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

    def add_magazine(cursor, name, publisher_id):
        try:
            cursor.execute("INSERT INTO magazines (magazine_name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        except sqlite3.IntegrityError:
            print(f"{name} is already in the database.")

    def add_subscriber(cursor, name, address):
        try:
            cursor.execute("INSERT INTO subscribers (subscriber_name, subscriber_address) VALUES (?, ?)", (name, address))
        except sqlite3.IntegrityError:
            print(f"A subscriber with name '{name}' and address '{address}' already exists.")

    def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", (subscriber_id, magazine_id, expiration_date))

    add_publisher(cursor, "Greatest Publisher of All Times")
    add_publisher(cursor, "Second Greatest Publisher")
    add_publisher(cursor, "A little Greater Publisher")

    add_magazine(cursor, "Outdoor Sports", 1)
    add_magazine(cursor, "Chess News", 2)
    add_magazine(cursor, "Cool Recipes", 3)

    add_subscriber(cursor, "Justin Case", "12345 NE 12th St")
    add_subscriber(cursor, "Marion Berry", "345 SW 40th Ave")
    add_subscriber(cursor, "Anonymous", "0000 XX Drive Neverland")

    add_subscription(cursor, 2, 3, "2025-12-31")
    add_subscription(cursor, 1, 2, "2025-05-31")
    add_subscription(cursor, 3, 3, "2025-10-15")
    add_subscription(cursor, 2, 1, "2025-11-11")

    conn.commit()

    cursor.execute("SELECT * FROM subscribers")
    print(cursor.fetchall())
    cursor.execute("SELECT * FROM magazines ORDER BY magazine_name")
    print(cursor.fetchall())
    cursor.execute("SELECT magazine_name FROM magazines WHERE publisher_id = 2")
    print(cursor.fetchall())