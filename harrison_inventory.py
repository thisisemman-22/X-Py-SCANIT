import sqlite3

# --- DATABASE SETUP ---
def connect_db():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        stock INTEGER NOT NULL,
        price REAL NOT NULL,
        barcode TEXT NOT NULL UNIQUE
    )
    ''')

# --- INVENTORY MANAGEMENT FUNCTIONS ---
def add_product(cursor, conn, product_name, stock, price, barcode):
    """Add a new product to the inventory."""
    try:
        cursor.execute('''
        INSERT INTO inventory (product_name, stock, price, barcode)
        VALUES (?, ?, ?, ?)
        ''', (product_name, stock, price, barcode))
        conn.commit()
        return {"message": f"Product {product_name} added to inventory."}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

def update_stock(cursor, conn, barcode, new_stock):
    """Update the stock of a product by its barcode."""
    try:
        cursor.execute('''
            UPDATE inventory SET stock = ? WHERE barcode = ?
        ''', (new_stock, barcode))
        conn.commit()
        return {"message": f"Stock updated for product with barcode {barcode}."}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

def fetch_inventory(cursor):
    """Fetch and display all products in the inventory."""
    try:
        cursor.execute('SELECT * FROM inventory')
        return cursor.fetchall()
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

def add_quantity(cursor, conn, barcode, quantity):
    """
    Update the quantity of a product in the inventory based on barcode.
    If the product exists, it updates the stock.
    If the product does not exist, it adds it with a default price.
    """
    try:
        cursor.execute('SELECT * FROM inventory WHERE barcode = ?', (barcode,))
        existing_product = cursor.fetchone()

        if existing_product:
            # Update stock if the product exists
            new_stock = existing_product[2] + quantity  # existing stock + new quantity
            cursor.execute('UPDATE inventory SET stock = ? WHERE product_id = ?', (new_stock, existing_product[0]))
            conn.commit()
            return {"message": f"Updated {existing_product[1]} stock to {new_stock}."}
        else:
            return {"error": "Product not found. Please add the product first."}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}

def get_product_names_by_barcodes(cursor, barcodes):
    """Fetch product names for the given barcodes."""
    try:
        cursor.execute('''
            SELECT product_name FROM inventory WHERE barcode IN ({})
        '''.format(','.join('?' * len(barcodes))), barcodes)
        return cursor.fetchall()
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
    
def get_price_by_barcode(cursor, barcode):
    """Fetch the price for the given barcode."""
    try:
        cursor.execute('''
            SELECT price FROM inventory WHERE barcode = ?
        ''', (barcode,))
        result = cursor.fetchone()
        if result:
            return {"price": result[0]}
        else:
            return {"error": "Product not found"}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
