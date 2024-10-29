from flask import Flask, request, jsonify
from harrison_database import connect_db, create_tables
from harrison_inventory import add_product, update_stock, fetch_inventory
from harrison_transaction import handle_transaction, generate_reports, notify_low_stock, total_sales, average_transaction_value, most_sold_products, sales_by_date
import os

app = Flask(__name__)

# Initialize database connection and create tables
conn, cursor = connect_db()
create_tables(cursor)
conn.close()  # Close the initial connection after creating tables

@app.route('/add_product', methods=['POST'])
def add_product_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    data = request.json
    product_name = data.get('product_name')
    stock = data.get('stock')
    price = data.get('price')
    barcode = data.get('barcode')
    result = add_product(cursor, conn, product_name, stock, price, barcode)
    conn.close()  # Close the connection after the operation
    return jsonify(result), 201 if 'message' in result else 400

@app.route('/update_stock', methods=['POST'])
def update_stock_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    data = request.json
    barcode = data.get('barcode')
    new_stock = data.get('new_stock')
    result = update_stock(cursor, conn, barcode, new_stock)
    conn.close()  # Close the connection after the operation
    return jsonify(result), 200 if 'message' in result else 400

@app.route('/fetch_inventory', methods=['GET'])
def fetch_inventory_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    inventory = fetch_inventory(cursor)
    conn.close()  # Close the connection after the operation
    # Extract values from the tuple
    inventory_data = [
        {
            "product_id": item[0],
            "product_name": item[1],
            "stock": item[2],
            "price": item[3],
            "barcode": item[4]
        } for item in inventory
    ]
    return jsonify(inventory_data)

@app.route('/handle_transaction', methods=['POST'])
def handle_transaction_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    result, status_code = handle_transaction(cursor, conn)
    conn.close()  # Close the connection after the operation
    return jsonify(result), status_code

@app.route('/generate_reports', methods=['GET'])
def generate_reports_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    result = generate_reports(cursor)
    conn.close()  # Close the connection after the operation
    return jsonify(result)

@app.route('/notify_low_stock', methods=['GET'])
def notify_low_stock_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    result = notify_low_stock(cursor)
    conn.close()  # Close the connection after the operation
    return jsonify(result), 200

@app.route('/total_sales', methods=['GET'])
def total_sales_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    result = total_sales(cursor)
    conn.close()  # Close the connection after the operation
    return jsonify(result), 200

@app.route('/average_transaction_value', methods=['GET'])
def average_transaction_value_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    result = average_transaction_value(cursor)
    conn.close()  # Close the connection after the operation
    return jsonify(result), 200

@app.route('/most_sold_products', methods=['GET'])
def most_sold_products_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    result = most_sold_products(cursor)
    conn.close()  # Close the connection after the operation
    return jsonify(result), 200

@app.route('/sales_by_date', methods=['GET'])
def sales_by_date_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    result = sales_by_date(cursor)
    conn.close()  # Close the connection after the operation
    return jsonify(result), 200

@app.route('/exit', methods=['POST'])
def exit_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    conn.close()
    return jsonify({"message": "Connection closed and program exited"}), 200

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)