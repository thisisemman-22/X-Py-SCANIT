from datetime import datetime
import sqlite3
import random
import string
import json
import qrcode
import os
from flask import request

store_id = "utangnginamo2024"

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

    for item in data.get('items', []):
        barcode = item.get('barcode')
        quantity = item.get('quantity')

        cursor.execute('''
            SELECT product_name, stock, price, barcode FROM inventory WHERE barcode = ?
        ''', (barcode,))
        product = cursor.fetchone()

        if not product:
            return {"error": "Product not found"}, 404

        product_name, stock, price, barcode = product

        if quantity > stock:
            return {"error": "Insufficient stock"}, 400

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