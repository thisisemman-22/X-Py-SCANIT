# '''
# PSEUDOCODE
#     START
#         IMPORT sqlite3
        
#         FUNCTION connect_db()
#             SET AND CALL conn = sqlite3.connect('inventory.db')
#             SET AND CALL cursor = conn.cursor()
#             RETURN conn, cursor
#         END FUNCTION

#         FUNCTION create_tables(cursor)
#             CALL cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS inventory (
#                     product_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     product_name TEXT NOT NULL,
#                     stock INTEGER NOT NULL,
#                     price REAL NOT NULL,
#                     barcode TEXT NOT NULL UNIQUE
#                 )
#             ''')
            
#             CALL cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS transactions (
#                     transaction_id TEXT PRIMARY KEY,
#                     total_amount REAL NOT NULL,
#                     transaction_date TEXT NOT NULL,
#                     payment_method TEXT NOT NULL,
#                     reference_number TEXT,
#                     items TEXT NOT NULL
#                 )
#             ''')

#             CALL cursor.connection.commit()
#         END FUNCTION
#     END

# '''


import sqlite3

# --- DATABASE CONNECTION ---
def connect_db():
    """Establish connection to the SQLite database."""
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    """Create the necessary tables if they don't exist."""
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        stock INTEGER NOT NULL,
        price REAL NOT NULL,
        barcode TEXT NOT NULL UNIQUE
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        transaction_id TEXT PRIMARY KEY,
        total_amount REAL NOT NULL,
        transaction_date TEXT NOT NULL,
        payment_method TEXT NOT NULL,
        reference_number TEXT,
        items TEXT NOT NULL
    )
    ''')

    # Commit the changes
    cursor.connection.commit()
