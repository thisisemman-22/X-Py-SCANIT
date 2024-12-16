'''
PSEUDOCODE
    START
        FROM flask IMPORT Flask, request, jsonify, send_from_directory
        FROM harrison_database IMPORT connect_db, create_tables
        FROM harrison_inventory IMPORT add_product, update_stock, fetch_inventory, get_product_names_by_barcodes, get_prices_by_barcodes, calculate_total_amount
        FROM harrison_transaction IMPORT handle_transaction, generate_reports, notify_low_stock, total_sales, average_transaction_value, most_sold_products, sales_by_date, get_transactions_by_date
        FROM flask_cors IMPORT CORS
        IMPORT os

        SET app = Flask(__name__)
        CALL CORS(app)

        SET AND CALL conn, cursor = connect_db()
        CALL create_tables(cursor)
        CALL conn.close()

        @app.route('/add_product', methods=['POST'])
        FUNCTION add_product_route()
            SET AND CALL conn, cursor = connect_db()
            SET data = request.json
            SET AND CALL product_name = data.get('product_name')
            SET AND CALL stock = data.get('stock')
            SET AND CALL price = data.get('price')
            SET AND CALL barcode = data.get('barcode')
            SET result = add_product(cursor, conn, product_name, stock, price, barcode)
            CALL conn.close()
            RETURN jsonify(result), 201 IF 'message' IN result ELSE 400
        END FUNCTION

        @app.route('/update_stock', methods=['POST'])
        FUNCTION update_stock_route()
            SET AND CALL conn, cursor = connect_db()
            SET data = request.json
            SET AND CALL barcode = data.get('barcode')
            SET AND CALL new_stock = data.get('new_stock')
            SET result = update_stock(cursor, conn, barcode, new_stock)
            CALL conn.close()
            RETURN jsonify(result), 200 IF 'message' IN result ELSE 400
        END FUNCTION

        @app.route('/fetch_inventory', methods=['GET'])
        FUNCTION fetch_inventory_route()
            SET AND CALL conn, cursor = connect_db()
            SET AND CALL inventory = fetch_inventory(cursor)
            CALL conn.close()
            SET inventory_data = [
                {
                    "product_id": item[0],
                    "product_name": item[1],
                    "stock": item[2],
                    "price": item[3],
                    "barcode": item[4]
                } FOR item IN inventory
                END FOR
            ]
            RETURN jsonify(inventory_data)
        END FUNCTION

        @app.route('/handle_transaction', methods=['POST'])
        FUNCTION handle_transaction_route()
            SET AND CALL conn, cursor = connect_db()
            SET AND CALL result, status_code = handle_transaction(cursor, conn)
            CALL conn.close()
            RETURN jsonify(result), status_code
        END FUNCTION

        @app.route('/generate_reports', methods=['GET'])
        FUNCTION generate_reports_route()
            SET AND CALL conn, cursor = connect_db()
            SET AND CALL result = generate_reports(cursor)
            CALL conn.close()
            RETURN jsonify(result)
        END FUNCTION

        @app.route('/notify_low_stock', methods=['GET'])
        FUNCTION notify_low_stock_route()
            SET AND CALL conn, cursor = connect_db()
            SET AND CALL result = notify_low_stock(cursor)
            CALL conn.close()
            RETURN jsonify(result), 200
        END FUNCTION

        @app.route('/total_sales', methods=['GET'])
        FUNCTION total_sales_route()
            SET AND CALL conn, cursor = connect_db()
            SET AND CALL result = total_sales(cursor)
            CALL conn.close()
            RETURN jsonify(result), 200
        END FUNCTION

        @app.route('/average_transaction_value', methods=['GET'])
        FUNCTION average_transaction_value_route()
            SET AND CALL conn, cursor = connect_db()
            SET AND CALL result = average_transaction_value(cursor)
            CALL conn.close()
            RETURN jsonify(result), 200
        END FUNCTION

        @app.route('/most_sold_products', methods=['GET'])
        FUNCTION most_sold_products_route()
            SET AND CALL conn, cursor = connect_db()
            SET AND CALL result = most_sold_products(cursor)
            CALL conn.close()
            RETURN jsonify(result), 200
        END FUNCTION

        @app.route('/sales_by_date', methods=['GET'])
        FUNCTION sales_by_date_route()
            SET AND CALL conn, cursor = connect_db()
            SET AND CALL result = sales_by_date(cursor)
            CALL conn.close()
            RETURN jsonify(result), 200
        END FUNCTION

        @app.route('/transactions_by_date', methods=['GET'])
        FUNCTION transactions_by_date_route()
            SET AND CALL date = request.args.get('date')
            IF NOT date
                RETURN jsonify({"error": "Date parameter is required"}), 400
            END IF

            SET AND CALL conn, cursor = connect_db()
            SET AND CALL transactions = get_transactions_by_date(cursor, date)
            CALL conn.close()
            RETURN jsonify(transactions), 200
        END FUNCTION

        @app.route('/get_product_names', methods=['POST'])
        FUNCTION get_product_names_route()
            SET AND CALL conn, cursor = connect_db()
            SET data = request.json
            SET AND CALL barcodes = data.get('barcodes')
            IF NOT barcodes
                RETURN jsonify({"error": "Barcodes parameter is required"}), 400
            END IF

            SET AND CALL result = get_product_names_by_barcodes(cursor, barcodes)
            CALL conn.close()

            IF isinstance(result, dict) AND 'error' IN result
                RETURN jsonify(result), 400
            END IF

            RETURN jsonify(result), 200
        END FUNCTION

        @app.route('/exit', methods=['POST'])
        FUNCTION exit_route()
            SET AND CALL conn, cursor = connect_db()
            CALL conn.close()
            RETURN jsonify({"message": "Connection closed and program exited"}), 200
        END FUNCTION

        @app.route('/qr_code/<filename>')
        FUNCTION serve_qr_code(filename)
            RETURN send_from_directory(os.path.join(app.root_path, 'static', 'qr_codes'), filename)
        END FUNCTION

        @app.route('/get_prices', methods=['POST'])
        FUNCTION get_prices_route()
            SET AND CALL conn, cursor = connect_db()
            SET data = request.json
            SET AND CALL barcodes = data.get('barcodes')
            IF NOT barcodes
                RETURN jsonify({"error": "Barcodes parameter is required"}), 400
            END IF

            SET AND CALL result = get_prices_by_barcodes(cursor, barcodes)
            CALL conn.close()

            IF isinstance(result, dict) AND 'error' IN result
                RETURN jsonify(result), 400
            END IF

            RETURN jsonify(result), 200
        END FUNCTION

        @app.route('/calculate_total', methods=['POST'])
        FUNCTION calculate_total_route()
            SET AND CALL conn, cursor = connect_db()
            SET data = request.json
            SET AND CALL barcodes = data.get('barcodes')
            SET AND CALL quantities = data.get('quantities')
            IF NOT barcodes OR NOT quantities OR len(barcodes) != len(quantities)
                RETURN jsonify({"error": "Barcodes and quantities must be provided and must have the same length"}), 400
            END IF

            SET AND CALL result = calculate_total_amount(cursor, barcodes, quantities)
            CALL conn.close()

            IF isinstance(result, dict) AND 'error' IN result
                RETURN jsonify(result), 400
            END IF

            RETURN jsonify(result), 200
        END FUNCTION

        IF __name__ EQUALS "__main__"
            SET port = INT(os.environ.get('PORT', 5000))
            CALL app.run(host='0.0.0.0', port=port, debug=True)
        END IF
    END
'''


from flask import Flask, request, jsonify, send_from_directory
from harrison_database import connect_db, create_tables
from harrison_inventory import add_product, update_stock, fetch_inventory, get_product_names_by_barcodes, get_prices_by_barcodes, calculate_total_amount
from harrison_transaction import handle_transaction, generate_reports, notify_low_stock, total_sales, average_transaction_value, most_sold_products, sales_by_date, get_transactions_by_date
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app) # enable CORS for all routes

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

@app.route('/transactions_by_date', methods=['GET'])
def transactions_by_date_route():
    date = request.args.get('date')
    if not date:
        return jsonify({"error": "Date parameter is required"}), 400
    
    conn, cursor = connect_db()  # Create a new connection and cursor
    transactions = get_transactions_by_date(cursor, date)
    conn.close()  # Close the connection after the operation
    return jsonify(transactions), 200

@app.route('/get_product_names', methods=['POST'])
def get_product_names_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    data = request.json
    barcodes = data.get('barcodes')
    if not barcodes:
        return jsonify({"error": "Barcodes parameter is required"}), 400

    result = get_product_names_by_barcodes(cursor, barcodes)
    conn.close()  # Close the connection after the operation

    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), 400

    return jsonify(result), 200

@app.route('/exit', methods=['POST'])
def exit_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    conn.close()
    return jsonify({"message": "Connection closed and program exited"}), 200

@app.route('/qr_code/<filename>')
def serve_qr_code(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'qr_codes'), filename)

@app.route('/get_prices', methods=['POST'])
def get_prices_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    data = request.json
    barcodes = data.get('barcodes')
    if not barcodes:
        return jsonify({"error": "Barcodes parameter is required"}), 400

    result = get_prices_by_barcodes(cursor, barcodes)
    conn.close()  # Close the connection after the operation

    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), 400

    return jsonify(result), 200

@app.route('/calculate_total', methods=['POST'])
def calculate_total_route():
    conn, cursor = connect_db()  # Create a new connection and cursor
    data = request.json
    barcodes = data.get('barcodes')
    quantities = data.get('quantities')
    if not barcodes or not quantities or len(barcodes) != len(quantities):
        return jsonify({"error": "Barcodes and quantities must be provided and must have the same length"}), 400

    result = calculate_total_amount(cursor, barcodes, quantities)
    conn.close()  # Close the connection after the operation

    if isinstance(result, dict) and 'error' in result:
        return jsonify(result), 400

    return jsonify(result), 200

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)