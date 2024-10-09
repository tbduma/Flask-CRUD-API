from flask import  Flask, request, jsonify

app = Flask(__name__)

# In-memory database for products (dictionary)
products = {}

# Add a product
@app.route('/products', methods=['POST'])
def add_product():
    product_id = request.json['id']
    product_info = request.json['info']
    products[product_id] = product_info
    return jsonify({'message': 'Product added successfully!'}), 201

# Get a product by ID
@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product), 200
    else:
        return jsonify({'message': 'Product not found'}), 404

# Update a product by ID
@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id in products:
        products[product_id] = request.json['info']
        return jsonify({'message': 'Product updated successfully!'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404

# Delete a product by ID
@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in products:
        del products[product_id]
        return jsonify({'message': 'Product deleted successfully!'}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)