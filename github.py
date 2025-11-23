class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name}: {self.price} руб."


class Order:
    def __init__(self):
        self.items = []
        self.total_cost = 0

    def add_product(self, product):
        self.items.append(product)
        self.total_cost += product.price

    def remove_product(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                self.total_cost -= product.price
                break

    def print_receipt(self):
        print("Чек заказа:")
        for product in self.items:
            print(product.get_info())
        print(f"Общая сумма: {self.total_cost} руб.")

t1 = Product("Хлеб", 50)
t2 = Product("Молоко", 70)
t3 = Product("Яблоки", 100)

order = Order()

order.add_product(t1)
order.add_product(t2)
order.add_product(t3)

order.print_receipt()
order.remove_product("Молоко")
order.print_receipt()