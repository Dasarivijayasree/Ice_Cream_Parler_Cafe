import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('ice_cream_parlor.db')
cursor = conn.cursor()

# Create the tables
cursor.execute('''CREATE TABLE IF NOT EXISTS SeasonalFlavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    ingredients TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Ingredients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    quantity INTEGER
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS CustomerSuggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    suggested_flavor TEXT,
    allergy_concern TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Allergens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Cart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_id INTEGER,
    FOREIGN KEY (flavor_id) REFERENCES SeasonalFlavors (id)
)''')

# Commit changes and close the connection
conn.commit()
conn.close()
