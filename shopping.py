class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def total_price(self):
        return self.price * self.quantity

    def display(self):
        print(f"Product: {self.name}")
        print(f"Price: ₱{self.price:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Subtotal: ₱{self.total_price():.2f}")
        print("-" * 20)

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"\nAdded {product.quantity} x {product.name} to cart.")

    def remove_product(self, index):
        removed = self.products.pop(index)
        print(f"\nRemoved {removed.name} from cart.")

    def view_cart(self):
        if not self.products:
            print("\nCart is empty.")
            return
        print("\n[Your Shopping Cart]")
        print("=" * 20)
        for product in self.products:
            product.display()
        print(f"Total: ₱{self.calculate_total():.2f}")
        print("=" * 20)

    def calculate_total(self):
        return sum(p.total_price() for p in self.products)

def is_valid_price(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def is_valid_quantity(value):
    try:
        val = int(value)
        return val > 0
    except ValueError:
        return False

def input_product():
    print("\n[Add Product]")
    name = input("Enter Product Name: ")
    price = input("Enter Product Price: ")
    while not is_valid_price(price):
        print("Invalid input. Please enter a valid price.")
        price = input("Enter Product Price: ")
    quantity = input("Enter Quantity: ")
    while not is_valid_quantity(quantity):
        print("Invalid input. Please enter a valid quantity.")
        quantity = input("Enter Quantity: ")
    return Product(name, price, quantity)

def main():
    cart = ShoppingCart()
    while True:
        print("=" * 30)
        print("{:^30}".format("Online Shopping Cart"))
        print("=" * 30)
        print("1. Add Product")
        print("2. Remove Product")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            product = input_product()
            cart.add_product(product)

        elif choice == "2":
            if not cart.products:
                print("\nCart is empty.")
                continue

            print("\n[Products in Cart]")
            for i, p in enumerate(cart.products, 1):
                print(f"{i}. {p.name} ({p.quantity} x ₱{p.price:.2f})")
            selected = input("Select product to remove: ")
            if selected.isdigit() and 1 <= int(selected) <= len(cart.products):
                cart.remove_product(int(selected)-1)
            else:
                print("Invalid selection.")

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            if not cart.products:
                print("\nCart is empty.")
            else:
                print("\n[Checkout]")
                cart.view_cart()
                print("Thank you for your purchase!")
                cart.products.clear()

        elif choice == "5":
            print("Exit Program")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
