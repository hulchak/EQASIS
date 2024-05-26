class Product:
    def __init__(self, name, price, product_type):
        self.name = name
        self.price = price
        self.product_type = product_type

class ProductCatalog:
    def __init__(self, products):
        self.products = products

    def search_product(self, query):
        # Реалізація пошуку продукту в каталозі
        return [product for product in self.products if query in product.name]

class ProductDisplay:
    @staticmethod
    def display_product(product):
        print(f"Product Name: {product.name}, Price: {product.price}, Type: {product.product_type}")

class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def place_order(self):
        # Логіка для розміщення замовлення
        print(f"Ordered {self.quantity} of {self.product.name}")

# Створення продуктів
products = [Product("Laptop", 1000, "Electronics"), Product("Smartphone", 700, "Electronics")]

# Каталог продуктів
catalog = ProductCatalog(products)
searched_products = catalog.search_product("Laptop")

# Відображення продуктів
for product in searched_products:
    ProductDisplay.display_product(product)

# Замовлення продукту
order = Order(searched_products[0], 2)
order.place_order()
