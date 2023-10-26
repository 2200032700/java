from behave import given, when, then

# Sample data to load
bdd_data = [
    {'product_name': 'Product A', 'category': 'Category X', 'availability': 'In Stock'},
    {'product_name': 'Product B', 'category': 'Category Y', 'availability': 'Out of Stock'},
    # Add more data entries as needed
]

@given('the following products are loaded')
def load_products(context):
    context.products = bdd_data  # Assign the sample data to the context

@when('I request the product by name {product_name}')
def request_product_by_name(context, product_name):
    context.requested_product = next((p for p in context.products if p['product_name'] == product_name), None)

@then('I should get the product with name {expected_product_name}')
def verify_product_by_name(context, expected_product_name):
    if context.requested_product:
        assert context.requested_product['product_name'] == expected_product_name
    else:
        assert False, "Product not found"

# Add more steps for other BDD scenarios as needed
