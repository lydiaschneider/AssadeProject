import sqlite3

# Connect to the database
conn = sqlite3.connect("medications.db")
cursor = conn.cursor()

# Sample data for the users table
users = [
    ("alice123", "hashedpassword1"),
    ("bob456", "hashedpassword2"),
    ("charlie789", "hashedpassword3"),
]

# Insert sample users
cursor.executemany("""
    INSERT INTO users (username, password_hash)
    VALUES (?, ?);
""", users)

transactions = [
    ("John Doe", "Alice", "2025-02-23", "Metformina _1000mg Tableta", "dispensed"),
    ("Jane Smith", "Bob", "2025-02-22", "Ibuprofeno _Jarabe frasco", "restocked"),
    ("Michael Johnson", "Charlie", "2025-02-21", "Amoxicilina _400mg Suspensión Frasco", "dispensed"),
    ("Emily Brown", "Alice", "2025-02-20", "Ciprofloxaciona _500mg Tableta", "restocked"),
]

cursor.executemany("""
    INSERT INTO transactions (patient_name, giver_name, date, medication_id, action)
    VALUES (?, ?, ?, ?, ?);
""", transactions)

# Insert medications
medications = [
    ("Metformina _1000mg Tableta", "1000mg per tablet", "tablet", 3, 1000),
    ("Metformina _500mg Tableta", "500mg per tablet", "tablet", 3, 1000),
    ("Glyburide _5mg Tableta", "5mg per tablet", "tablet", 3, 1000),
    ("Gabapentina _600mg Tableta", "600mg per tablet", "tablet", 3, 500),
    ("Cefalexina _500mg Capsula", "500mg per capsule", "capsule", 2, 200),
    ("Claritromicina _500mg Tableta", "500mg per tablet", "tablet", 2, 200),
    ("Ciprofloxacina _500mg Tableta", "500mg per tablet", "tablet", 2, 200),
    ("Levofloxacina _500mg Tableta", "500mg per tablet", "tablet", 2, 200),
    ("Amoxicilina _600mg Suspensión Frasco", "600mg per bottle", "suspension", 3, 100),
    ("Amoxicilina _400mg Suspensión Frasco", "400mg per bottle", "suspension", 3, 100),
    ("Cefalexina _250mg Suspensión Frasco", "250mg per bottle", "suspension", 3, 100),
    ("Cefadroxilo _250mg Suspensión Frasco", "250mg per bottle", "suspension", 3, 100),
    ("Lisinopril _20mg Tableta", "20mg per tablet", "tablet", 3, 500),
    ("Enalapril _20mg Tableta", "20mg per tablet", "tablet", 3, 500),
    ("Lansoprazol _30mg Capsula", "30mg per capsule", "capsule", 3, 1000),
    ("Omeprazol _20mg Capsula", "20mg per capsule", "capsule", 3, 1000),
    ("Clorfeniramina _Jarabe", "per bottle", "syrup", 2, 150),
    ("Ibuprofeno _800mg Tableta", "800mg per tablet", "tablet", 2, 300),
    ("Metronidazol _500mg Tableta", "500mg per tablet", "tablet", 2, 100),
    ("Minociclina _90mg Tableta", "90mg per tablet", "tablet", 1, 180),
    ("Cardioaspirina _81mg Tableta", "81mg per tablet", "tablet", 3, 500),
    ("Laxantes _Capsulas", "per capsule", "capsule", 2, 100),
    ("Triple antibiótico _Crema Tubo", "per tube", "cream", 3, 75),
    ("Hidrocortisona _Crema Tubo", "per tube", "cream", 2, 75),
    ("Clotrimazol _Crema Tubo", "per tube", "cream", 2, 75),
    ("Benzoato de bencilo _Loción frasco", "per bottle", "lotion", 1, 50),
    ("NyQuil _Jarabe Frasco", "per bottle", "syrup", 2, 125),
    ("DayQuil _Jarabe Frasco", "per bottle", "syrup", 2, 125),
    ("AJ Flujipect _Jarabe Frasco", "per bottle", "syrup", 2, 200),
    ("Fluticasona _Spray Inhalador", "per inhaler", "spray", 2, 50),
    ("Albuterol _Spray Inhalador", "per inhaler", "spray", 2, 50),
    ("Spiriva _Capsulas + Inhalador (caja)", "per box", "capsules + inhaler", 2, 25),
    ("Ambroxol _jarabe Frasco", "per bottle", "syrup", 2, 50),
    ("Dexametasona _Ampolla", "per ampoule", "ampoule", 3, 200),
    ("Piroxican _Ampolla", "per ampoule", "ampoule", 3, 200),
    ("Dipirona _Ampolla", "per ampoule", "ampoule", 3, 100),
    ("Ibersartan _150mg Tableta", "150mg per tablet", "tablet", 2, 500),
    ("Creon _Capsulas", "per capsule", "capsule", 2, 100),
    ("Prednisona _10mg Tableta", "10mg per tablet", "tablet", 1, 50),
    ("Fluconazol _100mg-150mg Tableta", "100mg-150mg per tablet", "tablet", 1, 25),
    ("Terbinafina _250mg Tableta", "250mg per tablet", "tablet", 1, 25),
    ("Diclofenaco _75mg Tableta", "75mg per tablet", "tablet", 2, 100),
    ("Cloranfenicol _Gotas Oftalmicas", "per bottle", "eye drops", 2, 50),
    ("Ketorolaco _Gotas Oftalmicas", "per bottle", "eye drops", 2, 50),
    ("Otik _Gotas Óticas", "per bottle", "ear drops", 2, 50),
    ("Ibuprofeno _Jarabe Frasco", "per bottle", "syrup", 3, 150),
    ("Acetaminofen _Jarabe Frasco", "per bottle", "syrup", 3, 200),
]

cursor.executemany("""
INSERT INTO medications (name, quantity_per_unit, form_of_medication, usage, avg_units_per_month)
VALUES (?, ?, ?, ?, ?)
""", medications)

conn.commit()
conn.close()

print("Database populated successfully.")
