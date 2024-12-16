# '''
# PSEUDOCODE
#     FROM datetime IMPORT datetime
#     IMPORT sqlite3
#     IMPORT random
#     IMPORT string
#     IMPORT json
#     IMPORT qrcode
#     IMPORT os
#     FROM flask IMPORT request

#     SET store_id = "da_shop.X-Py"

#     FUNCTION generate_transaction_id()
#         RETURN AND CALL ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
#     END FUNCTION

#     FUNCTION generate_qr_code(transaction_id, total_amount, payment_method, reference_number=None, items=None)
#         SET qr_data = {
#             "Store ID number": store_id,
#             "Transaction ID": transaction_id,
#             "Total Amount": total_amount,
#             "Payment Method": payment_method,
#             "Items": items
#         }

#         SET AND CALL qr = qrcode.QRCode(
#             version=1,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )

#         CALL qr.add_data(qr_data)
#         CALL qr.make(fit=True)

#         SET AND CALL img = qr.make_image(fill='black', back_color='white')
#         SET AND CALL qr_code_path = os.path.join('static', 'qr_codes', f"transaction_{transaction_id}.png")
#         CALL os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)
#         CALL img.save(qr_code_path)

#         RETURN f"/qr_code/transaction_{transaction_id}.png"
#     END FUNCTION

#     FUNCTION handle_transaction(cursor, conn)
#         SET data = request.json
#         SET AND CALL transaction_id = generate_transaction_id()
#         SET total_amount = 0
#         SET reference_number = None
#         SET items = {}

#         SET AND CALL barcodes = data.get('barcodes')
#         SET AND CALL quantities = data.get('quantities')

#         IF NOT barcodes OR NOT quantities OR len(barcodes) != len(quantities) THEN
#             RETURN {"error": "Barcodes and quantities must be provided and must have the same length"}, 400
#         END IF

#         FOR barcode, quantity IN zip(barcodes, quantities)
#             CALL cursor.execute('''
#                 SELECT product_name, stock, price, barcode FROM inventory WHERE barcode = ?
#             ''', (barcode,))
#             SET AND CALL product = cursor.fetchone()

#             IF NOT product
#                 RETURN {"error": f"Product with barcode {barcode} not found"}, 404
#             END IF

#             SET product_name, stock, price, barcode = product

#             IF quantity > stock
#                 RETURN {"error": f"Insufficient stock for product {product_name}"}, 400
#             END IF

#             SET new_stock = stock - quantity
#             CALL cursor.execute('''
#                 UPDATE inventory SET stock = ? WHERE barcode = ?
#             ''', (new_stock, barcode))

#             SET total_amount += price * quantity

#             IF barcode IN items
#                 SET items[barcode]['quantity'] += quantity
#             ELSE
#                 SET items[barcode] = {
#                     'product_name': product_name,
#                     'quantity': quantity,
#                     'price': price
#                 }
#             END IF
#         END FOR

#         IF total_amount == 0
#             RETURN {"error": "No items were added to the transaction"}, 400
#         END IF

#         SET payment_method = data.get('payment_method')
#         IF payment_method NOT IN ['cash', 'qrph']
#             RETURN {"error": "Invalid payment method"}, 400
#         END IF

#         IF payment_method == 'cash
#             SET AND CALL cash_received = data.get('cash_received')
#             IF cash_received < total_amount
#                 RETURN {"error": "Insufficient cash"}, 400
#             END IF
#             SET change = cash_received - total_amount
#             SET response = {
#                 "message": "Transaction completed",
#                 "total_amount": round(total_amount, 2),
#                 "change": round(change, 2),
#                 "payment_method": payment_method
#             }
#         ELSE IF payment_method == 'qrph'
#             SET AND CALL qr_code_path = generate_qr_code(transaction_id, total_amount, payment_method, items=items)
#             SET base_url = request.host_url.rstrip('/')
#             SET qr_code_url = f"{base_url}{qr_code_path}"
#             SET response = {
#                 "message": "QR code generated",
#                 "qr_code_url": qr_code_url
#             }
#         END IF

#         SET AND CALL transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         SET AND CALL items_json = json.dumps(items)
#         CALL cursor.execute('''
#             INSERT INTO transactions (transaction_id, total_amount, transaction_date, payment_method, reference_number, items)
#             VALUES (?, ?, ?, ?, ?, ?)
#         ''', (transaction_id, total_amount, transaction_date, payment_method, reference_number, items_json))
#         CALL conn.commit()

#         RETURN response, 200
#     END FUNCTION

#     FUNCTION generate_reports(cursor)
#         SET AND CALL today = datetime.now().strftime('%Y-%m-%d')
#         CALL cursor.execute('''
#             SELECT product_name, stock FROM inventory
#         ''')

#         SET AND CALL report = [{"product_name": row[0], "stock": row[1]} FOR row IN cursor.fetchall() END FOR]
#         SET AND CALL formatted_report = "\n".join([f"Product: {item['product_name']}, Stock: {item['stock']}" FOR item IN report])
#         RETURN {"report": formatted_report, "date": today}
#     END FUNCTION

#     FUNCTION notify_low_stock(cursor)
#         SET low_stock_threshold = 10
#         CALL cursor.execute('''
#             SELECT product_name, stock FROM inventory WHERE stock < ?
#         ''', (low_stock_threshold,))
#         SET AND CALL low_stock_items = [{"product_name": item[0], "stock": item[1]} FOR item IN cursor.fetchall()]
#         RETURN {"low_stock_items": low_stock_items}
#     END FUNCTION

#     FUNCTION total_sales(cursor)
#         CALL cursor.execute('''
#             SELECT SUM(total_amount) FROM transactions
#         ''')
#         SET AND CALL total = cursor.fetchone()[0]
#         SET AND CALL total = round(total, 2)
#         RETURN total
#     END FUNCTION

#     FUNCTION average_transaction_value(cursor)
#         CALL cursor.execute('''
#             SELECT AVG(total_amount) FROM transactions
#         ''')
#         SET AND CALL avg_value = cursor.fetchone()[0]
#         SET AND CALL avg_value = round(avg_value, 2)
#         RETURN avg_value
#     END FUNCTION

#     FUNCTION most_sold_products(cursor)
#         CALL cursor.execute('''
#             SELECT items FROM transactions
#         ''')
#         SET AND CALL all_items = cursor.fetchall()
#         SET product_sales = {}
#         FOR items_json IN all_items
#             SET AND CALL items = json.loads(items_json[0])
#             FOR barcode, item IN items.items()
#                 IF barcode IN product_sales
#                     SET product_sales[barcode]['quantity'] += item['quantity']
#                 ELSE
#                     SET product_sales[barcode] = {
#                         'product_name': item['product_name'],
#                         'quantity': item['quantity']
#                     }
#                 END IF
#             END FOR
#         END FOR
#         SET AND CALL sorted_products = sorted(product_sales.items(), key=lambda x: x[1]['quantity'], reverse=True)
#         SET AND CALL most_sold = [{"product_name": product['product_name'], "barcode": barcode, "quantity_sold": product['quantity']} FOR barcode, product IN sorted_products END FOR]
#         RETURN most_sold
#     END FUNCTION

#     FUNCTION sales_by_date(cursor)
#         CALL cursor.execute('''
#             SELECT transaction_date, SUM(total_amount) FROM transactions GROUP BY DATE(transaction_date)
#         ''')
#         SET AND CALL sales = [{"date": date, "total_sales": round(total, 2)} FOR date, total IN cursor.fetchall() END FOR]
#         RETURN sales
#     END FUNCTION

#     FUNCTION get_transactions_by_date(cursor, date)
#         CALL cursor.execute('''
#             SELECT transaction_id, total_amount, transaction_date, payment_method, items
#             FROM transactions
#             WHERE DATE(transaction_date) = ?
#         ''', (date,))
#       SET AND CALL transactions = cursor.fetchall()
#       SET transaction_list = [
#           {
#               "transaction_id": row[0],
#               "total_amount": row[1],
#               "transaction_date": row[2],
#               "payment_method": row[3],
#               "items": [item["product_name"] FOR item IN json.loads(row[4]).values()]
#           }
#           FOR row IN transactions
#       END FOR
#       ]
#       RETURN transaction_list
#     END FUNCTION
# END
# '''

from datetime import datetime
import random
import string
import json
import qrcode
import os
from flask import request

store_id = "da_shop.X-Py"

# --- TRANSACTION HANDLING ---
def generate_transaction_id():
    """Generate a unique transaction ID."""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

def generate_qr_code(transaction_id, total_amount, payment_method, reference_number=None, items=None):
    qr_data = {
        "Store ID number": store_id,
        "Transaction ID": transaction_id,
        "Total Amount": total_amount,
        "Payment Method": payment_method,
        "Items": items
    }

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    qr_code_path = os.path.join('static', 'qr_codes', f"transaction_{transaction_id}.png")
    os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)
    img.save(qr_code_path)

    return f"/qr_code/transaction_{transaction_id}.png"

def handle_transaction(cursor, conn):
    data = request.json
    transaction_id = generate_transaction_id()
    total_amount = 0
    reference_number = None
    items = {}

    barcodes = data.get('barcodes')
    quantities = data.get('quantities')

    if not barcodes or not quantities or len(barcodes) != len(quantities):
        return {"error": "Barcodes and quantities must be provided and must have the same length"}, 400

    for barcode, quantity in zip(barcodes, quantities):
        cursor.execute('''
            SELECT product_name, stock, price, barcode FROM inventory WHERE barcode = ?
        ''', (barcode,))
        product = cursor.fetchone()

        if not product:
            return {"error": f"Product with barcode {barcode} not found"}, 404

        product_name, stock, price, barcode = product

        if quantity > stock:
            return {"error": f"Insufficient stock for product {product_name}"}, 400

        new_stock = stock - quantity
        cursor.execute('''
            UPDATE inventory SET stock = ? WHERE barcode = ?
        ''', (new_stock, barcode))

        total_amount += price * quantity

        if barcode in items:
            items[barcode]['quantity'] += quantity
        else:
            items[barcode] = {
                'product_name': product_name,
                'quantity': quantity,
                'price': price
            }

    if total_amount == 0:
        return {"error": "No items were added to the transaction"}, 400

    payment_method = data.get('payment_method')
    if payment_method not in ['cash', 'qrph']:
        return {"error": "Invalid payment method"}, 400

    if payment_method == 'cash':
        cash_received = data.get('cash_received')
        if cash_received < total_amount:
            return {"error": "Insufficient cash"}, 400
        change = cash_received - total_amount
        response = {
            "message": "Transaction completed",
            "total_amount": round(total_amount, 2),
            "change": round(change, 2),
            "payment_method": payment_method
        }
    elif payment_method == 'qrph':
        qr_code_path = generate_qr_code(transaction_id, total_amount, payment_method, items=items)
        base_url = request.host_url.rstrip('/')
        qr_code_url = f"{base_url}{qr_code_path}"
        response = {
            "message": "QR code generated",
            "qr_code_url": qr_code_url
        }

    transaction_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    items_json = json.dumps(items)
    cursor.execute('''
        INSERT INTO transactions (transaction_id, total_amount, transaction_date, payment_method, reference_number, items)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (transaction_id, total_amount, transaction_date, payment_method, reference_number, items_json))
    conn.commit()

    return response, 200

def generate_reports(cursor):
    today = datetime.now().strftime('%Y-%m-%d')
    cursor.execute('''
        SELECT product_name, stock FROM inventory
    ''')

    report = [{"product_name": row[0], "stock": row[1]} for row in cursor.fetchall()]
    formatted_report = "\n".join([f"Product: {item['product_name']}, Stock: {item['stock']}" for item in report])
    return {"report": formatted_report, "date": today}

def notify_low_stock(cursor):
    low_stock_threshold = 10
    cursor.execute('''
        SELECT product_name, stock FROM inventory WHERE stock < ?
    ''', (low_stock_threshold,))

    low_stock_items = [{"product_name": item[0], "stock": item[1]} for item in cursor.fetchall()]
    return {"low_stock_items": low_stock_items}

def total_sales(cursor):
    cursor.execute('''
        SELECT SUM(total_amount) FROM transactions
    ''')
    total = cursor.fetchone()[0]
    total = round(total, 2)
    return total

def average_transaction_value(cursor):
    cursor.execute('''
        SELECT AVG(total_amount) FROM transactions
    ''')
    avg_value = cursor.fetchone()[0]
    avg_value = round(avg_value, 2)
    return avg_value

def most_sold_products(cursor):
    cursor.execute('''
        SELECT items FROM transactions
    ''')
    all_items = cursor.fetchall()
    product_sales = {}
    for items_json in all_items:
        items = json.loads(items_json[0])
        for barcode, item in items.items():
            if barcode in product_sales:
                product_sales[barcode]['quantity'] += item['quantity']
            else:
                product_sales[barcode] = {
                    'product_name': item['product_name'],
                    'quantity': item['quantity']
                }
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1]['quantity'], reverse=True)
    most_sold = [{"product_name": product['product_name'], "barcode": barcode, "quantity_sold": product['quantity']} for barcode, product in sorted_products]
    return most_sold

def sales_by_date(cursor):
    cursor.execute('''
        SELECT transaction_date, SUM(total_amount) FROM transactions GROUP BY DATE(transaction_date)
    ''')
    sales = [{"date": date, "total_sales": round(total, 2)} for date, total in cursor.fetchall()]
    return sales

def get_transactions_by_date(cursor, date):
    """Retrieve transactions for a specific date."""
    cursor.execute('''
        SELECT transaction_id, total_amount, transaction_date, payment_method, items
        FROM transactions
        WHERE DATE(transaction_date) = ?
    ''', (date,))
    
    transactions = cursor.fetchall()
    transaction_list = [
        {
            "transaction_id": row[0],
            "total_amount": row[1],
            "transaction_date": row[2],
            "payment_method": row[3],
            "items": [item["product_name"] for item in json.loads(row[4]).values()]
        }
        for row in transactions
    ]
    return transaction_list