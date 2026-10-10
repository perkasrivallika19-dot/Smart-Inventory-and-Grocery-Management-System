
class Product:
    def __init__(self, products=None):
        self.products = products if products is not None else {}

    def add_product(self):
        pid = input("Product ID: ").strip()

        if not pid:
            print("Product ID cannot be empty!")
            return

        if pid in self.products:
            print("Product ID already exists!")
            return

        name = input("Product Name: ").strip()

        if not name:
            print("Product name cannot be empty!")
            return

        try:
            price = float(input("Price: "))
            quantity = int(input("Quantity: "))

            if price <= 0 or quantity <= 0:
                print("Price and quantity must be positive!")
                return

        except ValueError:
            print("Invalid input! Enter a number for price and quantity.")
            return

        self.products[pid] = [name, price, quantity]
        print("Product added successfully!")

    def view_products(self):
        if not self.products:
            print("No products available!")
            return

        print("\nID | Name | Price | Quantity")
        print("-" * 35)

        for pid, p in self.products.items():
            print(pid, "|", p[0], "|", p[1], "|", p[2])

    def sell_product(self):
        pid = input("Product ID: ").strip()

        if pid not in self.products:
            print("Product not found!")
            return

        try:
            qty = int(input("Quantity to sell: "))

            if qty <= 0:
                print("Quantity must be greater than zero!")
                return

        except ValueError:
            print("Invalid quantity! Enter a whole number.")
            return

        p = self.products[pid]

        if qty > p[2]:
            print("Insufficient stock!")
            print("Available quantity:", p[2])
            return

        p[2] -= qty
        total = p[1] * qty

        print("Total bill: Rs.", total)
        print("Remaining stock:", p[2])


class Grocery(Product):
    def __init__(self):
        super().__init__({
            "101": ["Rice", 60, 10],
            "102": ["Sugar", 45, 20],
            "103": ["Milk", 30, 15],
            "104": ["Cooking Oil", 150, 8],
            "105": ["Wheat Flour", 50, 12]
        })


class Inventory(Product):
    def __init__(self):
        super().__init__({
            "101":["Laptop",50000,10],
            "102":["Mouse",20000,5],
            "103":["CPU",80000,15]
        })


# Main menu
grocery = Grocery()
inventory = Inventory()

while True:
    print("\n================Smart Product Management System===================")
    print("1. Groceries")
    print("2. General Inventory")
    print("3. Exit")

    category = input("Select category: ").strip()

    if category == "1":
        obj = grocery
        print("\n=================Grocery Management System====================")
    elif category == "2":
        obj = inventory
        print("\n=================Inventory Management System==================")
    elif category == "3":
        print("Thank you for using the system!")
        break
    else:
        print("Invalid category! Select 1, 2, or 3.")
        continue

    while True:
        print("\n1. Add Product")
        print("2. View Products")
        print("3. Sell Product")
        print("4. Back to Categories")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            obj.add_product()
        elif choice == "2":
            obj.view_products()
        elif choice == "3":
            obj.sell_product()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Select 1, 2, 3, or 4.")