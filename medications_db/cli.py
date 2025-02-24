import sqlite3
import getpass

# Connect to the database
conn = sqlite3.connect("medications.db")
cursor = conn.cursor()

def login():
    """Handles giver login."""
    while True:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()

        cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, password))
        user = cursor.fetchone()

        if user:
            print(f"\n✅ Welcome, {username}!\n")
            return username
        else:
            print("Invalid username or password. Try again.")

def show_medications():
    """Displays medications and stock levels."""
    print("Current Medication Stock:")
    cursor.execute("SELECT med_id, name, stock_levels FROM medications")
    meds = cursor.fetchall()

    if not meds:
        print("No medications available.")
        return []

    for med_id, name, stock in meds:
        print(f"[{med_id}] {name} - {stock} units left")

    return meds

def update_stock(username):
    """Handles dispensing and restocking medications."""
    meds = show_medications()
    
    if not meds:
        return

    try:
        med_id = int(input("\nEnter the Medication ID to update: ").strip())
        action = input("Enter 'dispense' or 'restock': ").strip().lower()

        # Validate input
        if action not in ["dispense", "restock"]:
            print("⚠️ Invalid action. Please enter 'dispense' or 'restock'.")
            return

        amount = int(input("Enter the quantity: ").strip())

        # Convert action to match database constraints
        action_db = "dispensed" if action == "dispense" else "restocked"

        # Fetch the current stock level
        cursor.execute("SELECT name, stock_levels FROM medications WHERE med_id = ?", (med_id,))
        med = cursor.fetchone()

        if not med:
            print("⚠️ Medication ID not found.")
            return

        med_name, stock = med

        if action == "dispense":
            if amount > stock:
                print("⚠️ Not enough stock to dispense.")
                return
            new_stock = stock - amount
        else:  # Restock
            new_stock = stock + amount

        # Update stock levels
        cursor.execute("UPDATE medications SET stock_levels = ? WHERE med_id = ?", (new_stock, med_id))
        
        # Log transaction
        cursor.execute("""
            INSERT INTO transactions (patient_name, giver_name, medication_id, action, date)
            VALUES (?, ?, ?, ?, DATE('now'))
        """, ("Unknown", username, med_id, action_db))

        conn.commit()
        print(f"✅ {amount} units {'dispensed from' if action == 'dispense' else 'added to'} {med_name}. New stock: {new_stock}")

    except ValueError:
        print("⚠️ Invalid input. Please enter numeric values where required.")

        
def main():
    """Main CLI loop."""
    print("\n📋 Welcome to the Medication Inventory CLI")
    username = login()

    while True:
        print("\nOptions:")
        print("1️⃣ View Medications")
        print("2️⃣ Dispense or Restock")
        print("3️⃣ Exit")
        
        choice = input("\nSelect an option: ").strip()

        if choice == "1":
            show_medications()
        elif choice == "2":
            update_stock(username)
        elif choice == "3":
            print("\n👋 Exiting. Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()

# Close connection when done
conn.close()
