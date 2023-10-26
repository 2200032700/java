from faker import Faker

fake = Faker()

class ProductFactory:
    @staticmethod
    def create_fake_product():
        product_name = fake.word()
        product_price = fake.random_number()
        product_category = fake.random_element(elements=("Electronics", "Clothing", "Home", "Books"))
        product_availability = fake.random_element(elements=("In Stock", "Out of Stock"))

        # Create and return a dictionary representing the fake product
        return {
            "name": product_name,
            "price": product_price,
            "category": product_category,
            "availability": product_availability
        }
