from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
products = [
    {
        'id': 1,
        'name': 'Product A',
        'category': 'Category X',
        'availability': 'In Stock'
    },
    {
        'id': 2,
        'name': 'Product B',
        'category': 'Category Y',
        'availability': 'Out of Stock'
    },
    # Add more product entries
]

@app.route('/read/<int:id>', methods=['GET'])
def read_product(id):
    product = next((p for p in products if p['id'] == id), None)
    if product:
        return jsonify(product)
    return "Product not found", 404

@app.route('/update/<int:id>', methods=['PUT'])
def update_product(id):
    # Update product logic here
    return "Product updated successfully"

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_product(id):
    # Delete product logic here
    return "Product deleted successfully"

@app.route('/list_all', methods=['GET'])
def list_all_products():
    return jsonify(products)

@app.route('/list_by_name/<name>', methods=['GET'])
def list_products_by_name(name):
    filtered_products = [p for p in products if p['name'] == name]
    return jsonify(filtered_products)

@app.route('/list_by_category/<category>', methods=['GET'])
def list_products_by_category(category):
    filtered_products = [p for p in products if p['category'] == category]
    return jsonify(filtered_products)

@app.route('/list_by_availability/<availability>', methods=['GET'])
def list_products_by_availability(availability):
    filtered_products = [p for p in products if p['availability'] == availability]
    return jsonify(filtered_products)

if __name__ == '__main__':
    app.run()
