import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("medications.db")
cursor = conn.cursor()

# Create tables
cursor.executescript("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS medications (
    med_id INTEGER PRIMARY KEY AUTOINCREMENT,                 
    name TEXT NOT NULL,
    quantity_per_unit TEXT,
    form_of_medication TEXT,                                  
    usage TEXT,
    avg_units_per_month INTEGER,                 
    stock_levels INTEGER CHECK (stock_levels >= 0),
    date_last_stocked DATE
);

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,                 
    patient_name TEXT,
    giver_name TEXT,
    date DATE DEFAULT CURRENT_DATE,
    medication_id INTEGER,
    action TEXT CHECK (action IN ('dispensed', 'restocked'))                                                
);
""")

conn.commit()
conn.close()

print("Database and tables created successfully.")
