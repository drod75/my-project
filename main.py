# main.py
import sqlite3

DB_NAME = "mydatabase.db"

def fetch_and_print_data():
    """
    Connects to the SQLite database, fetches data from the 'users' table,
    and prints it in a pretty format using the tabulate library.
    Includes a fallback for basic printing if tabulate is not available.
    """
    conn = None  # Initialize connection to None
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        print(f"Connected to database '{DB_NAME}' to fetch data.")

        # Fetch all data from the users table
        cursor.execute("SELECT id, name, email, age, city FROM users")
        rows = cursor.fetchall() # Fetches all rows from the query result

        if not rows:
            print("No data found in the 'users' table.")
            return

        try:
            # Try to use tabulate for pretty printing
            from tabulate import tabulate
            headers = ["ID", "Name", "Email", "Age", "City"]
            print("\n--- User Data (Formatted with Tabulate) ---")
            # "grid", "pipe", "orgtbl", "rst", "psql", "simple" are some tablefmt options
            print(tabulate(rows, headers=headers, tablefmt="grid"))
            print("-------------------------------------------\n")
        except ImportError:
            # Fallback to basic printing if tabulate is not installed
            print("\n--- User Data (Basic Print - 'tabulate' not found) ---")
            print(f"{'ID':<4} | {'Name':<20} | {'Email':<25} | {'Age':<5} | {'City':<15}")
            print("-" * 80)
            for row in rows:
                # Ensure all parts of the row are strings for formatting, handling None
                formatted_row = [str(item) if item is not None else "" for item in row]
                print(f"{formatted_row[0]:<4} | {formatted_row[1]:<20} | {formatted_row[2]:<25} | {formatted_row[3]:<5} | {formatted_row[4]:<15}")
            print("-" * 80)
            print("\nConsider installing 'tabulate' for better output: pip install tabulate\n")


    except sqlite3.Error as e:
        print(f"SQLite error during fetch: {e}")
    finally:
        # Close the database connection
        if conn:
            conn.close()
            print("Database connection closed after fetching.")

if __name__ == "__main__":
    fetch_and_print_data()