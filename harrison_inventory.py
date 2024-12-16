"""
PSEUDOCODE:
    IMPORT sqlite3

    FUNCTION connect_db()
        SET AND CALL conn = sqlite3.connect('inventory.db')
        SET AND CALL cursor = conn.cursor()
        RETURN conn, cursor
    END FUNCTION

    FUNCTION create_tables(cursor)
        CALL cursor.execute('''
            CREATE TABLE IF NOT EXISTS inventory (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                stock INTEGER NOT NULL,
                price REAL NOT NULL,
                barcode TEXT NOT NULL UNIQUE
            )
        ''')
    END FUNCTION

    FUNCTION add_product(cursor, conn, product_name, stock, price, barcode)
        TRY
            CALL cursor.execute('''
                INSERT INTO inventory (product_name, stock, price, barcode)
                VALUES (?, ?, ?, ?)
            ''', (product_name, stock, price, barcode))
            CALL conn.commit()
            RETURN {"message": f"Product {product_name} added to inventory."}
        EXCEPT sqlite3.Error AS e
            RETURN {"error": f"Database error: {e}"}
        EXCEPT Exception AS e
            RETURN {"error": f"An unexpected error occurred: {e}"}
        END TRY
    END FUNCTION

    FUNCTION update_stock(cursor, conn, barcode, new_stock)
        TRY
            CALL cursor.execute('''
                UPDATE inventory SET stock = ? WHERE barcode = ?
            ''', (new_stock, barcode))
            CALL conn.commit()
            RETURN {"message": f"Stock updated for product with barcode {barcode}."}
        EXCEPT sqlite3.Error AS e
            RETURN {"error": f"Database error: {e}"}
        EXCEPT Exception AS e
            RETURN {"error": f"An unexpected error occurred: {e}"}
        END TRY
    END FUNCTION

    FUNCTION fetch_inventory(cursor)
        TRY
            CALL cursor.execute('SELECT * FROM inventory')
            RETURN cursor.fetchall()
        EXCEPT sqlite3.Error AS e
            RETURN {"error": f"Database error: {e}"}
        EXCEPT Exception AS e
            RETURN {"error": f"An unexpected error occurred: {e}"}
        END TRY
    END FUNCTION

    FUNCTION add_quantity(cursor, conn, barcode, quantity)
        TRY
            CALL cursor.execute('SELECT * FROM inventory WHERE barcode = ?', (barcode,))
            SET existing_product = cursor.fetchone()

            IF existing_product
                SET new_stock = existing_product[2] + quantity
                CALL cursor.execute('UPDATE inventory SET stock = ? WHERE product_id = ?', (new_stock, existing_product[0]))
                CALL conn.commit()
                RETURN {"message": f"Updated {existing_product[1]} stock to {new_stock}."}
            ELSE
                RETURN {"error": "Product not found. Please add the product first."}
            END IF
        EXCEPT sqlite3.Error AS e
            RETURN {"error": f"Database error: {e}"}
        EXCEPT Exception AS e
            RETURN {"error": f"An unexpected error occurred: {e}"}
        END TRY
    END FUNCTION

    FUNCTION get_product_names_by_barcodes(cursor, barcodes)
        TRY
            CALL cursor.execute('''
                SELECT barcode, product_name FROM inventory WHERE barcode IN ({})
            '''.format(','.join('?' * len(barcodes))), barcodes)
            SET results = cursor.fetchall()

            IF NOT results
                RETURN {"error": "No products found for the given barcodes"}

            SET barcode_name_map = {barcode: name for barcode, name in results}
            SET product_names = [barcode_name_map.get(barcode, "Product not found") for barcode in barcodes]
            RETURN product_names
        EXCEPT sqlite3.Error AS e
            RETURN {"error": f"Database error: {e}"}
        EXCEPT Exception AS e
            RETURN {"error": f"An unexpected error occurred: {e}"}
        END TRY
    END FUNCTION

    FUNCTION get_prices_by_barcodes(cursor, barcodes)
        TRY
            CALL cursor.execute('''
                SELECT barcode, price FROM inventory WHERE barcode IN ({})
            '''.format(','.join('?' * len(barcodes))), barcodes)
            SET results = cursor.fetchall()

            IF results
                RETURN [{"barcode": barcode, "price": price} for barcode, price in results]
            ELSE
                RETURN {"error": "No products found for the given barcodes"}
            END IF
        EXCEPT sqlite3.Error AS e
            RETURN {"error": f"Database error: {e}"}
        EXCEPT Exception AS e
            RETURN {"error": f"An unexpected error occurred: {e}"}
        END TRY
    END FUNCTION

    FUNCTION calculate_total_amount(cursor, barcodes, quantities)
        TRY
            CALL cursor.execute('''
                SELECT barcode, price FROM inventory WHERE barcode IN ({})
            '''.format(','.join('?' * len(barcodes))), barcodes)
            SET AND CALL results = cursor.fetchall()

            IF NOT results
                RETURN {"error": "No products found for the given barcodes"}

            SET total_amount = 0
            SET barcode_price_map = {barcode: price for barcode, price in results}
            FOR EACH barcode, quantity IN ZIP(barcodes, quantities)
                IF barcode IN barcode_price_map
                    SET total_amount += barcode_price_map[barcode] * quantity
                ELSE
                    RETURN {"error": f"Product with barcode {barcode} not found"}
                END IF
            END FOR

            RETURN {"total_amount": round(total_amount, 2)}
        EXCEPT sqlite3.Error AS e
            RETURN {"error": f"Database error: {e}"}
        EXCEPT Exception AS e
            RETURN {"error": f"An unexpected error occurred: {e}"}
        END TRY
    END FUNCTION
END
"""

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
            SELECT barcode, product_name FROM inventory WHERE barcode IN ({})
        '''.format(','.join('?' * len(barcodes))), barcodes)
        results = cursor.fetchall()
        if not results:
            return {"error": "No products found for the given barcodes"}

        barcode_name_map = {barcode: name for barcode, name in results}
        product_names = [barcode_name_map.get(barcode, "Product not found") for barcode in barcodes]
        return product_names
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
    
def get_prices_by_barcodes(cursor, barcodes):
    """Fetch prices for the given barcodes."""
    try:
        cursor.execute('''
            SELECT barcode, price FROM inventory WHERE barcode IN ({})
        '''.format(','.join('?' * len(barcodes))), barcodes)
        results = cursor.fetchall()
        if results:
            return [{"barcode": barcode, "price": price} for barcode, price in results]
        else:
            return {"error": "No products found for the given barcodes"}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
    

def calculate_total_amount(cursor, barcodes, quantities):
    """Calculate the total amount for the given barcodes and quantities."""
    try:
        cursor.execute('''
            SELECT barcode, price FROM inventory WHERE barcode IN ({})
        '''.format(','.join('?' * len(barcodes))), barcodes)
        results = cursor.fetchall()
        if not results:
            return {"error": "No products found for the given barcodes"}

        total_amount = 0
        barcode_price_map = {barcode: price for barcode, price in results}
        for barcode, quantity in zip(barcodes, quantities):
            if barcode in barcode_price_map:
                total_amount += barcode_price_map[barcode] * quantity
            else:
                return {"error": f"Product with barcode {barcode} not found"}

        return {"total_amount": round(total_amount, 2)}
    except sqlite3.Error as e:
        return {"error": f"Database error: {e}"}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}
