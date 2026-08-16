from flask import Flask, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 599, "stock": 120},
    {"id": 2, "name": "Mechanical Keyboard", "price": 2499, "stock": 45},
    {"id": 3, "name": "USB-C Hub", "price": 999, "stock": 78},
    {"id": 4, "name": "Laptop Stand", "price": 799, "stock": 60},
]

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Mini E-commerce API", "status": "running"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/products/<int:product_id>")
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
