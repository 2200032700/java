Feature: Product Management

  Scenario: Read a Product
    Given the following products are loaded
    When I request the product by name "Product A"
    Then I should get the product with name "Product A"

  Scenario: Update a Product
    Given the following products are loaded
    When I update the product with name "Product B"
    And I request the product by name "Product B"
    Then I should get the updated product information

  Scenario: Delete a Product
    Given the following products are loaded
    When I delete the product with name "Product C"
    And I request the product by name "Product C"
    Then I should not find the product

  Scenario: List All Products
    Given the following products are loaded
    When I list all products
    Then I should see a list of products

  Scenario: Search Products by Name
    Given the following products are loaded
    When I search for products by name "Product X"
    Then I should see a list of products with matching names

  Scenario: Search Products by Category
    Given the following products are loaded
    When I search for products by category "Category Y"
    Then I should see a list of products in "Category Y"

  Scenario: Search Products by Availability
    Given the following products are loaded
    When I search for products by availability "In Stock"
    Then I should see a list of products that are "In Stock"
