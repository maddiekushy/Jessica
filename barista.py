
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    def __init__(self):
        self.receipt = []

    def add_item(self, item):
        self.receipt.append(item)

    def calculate_taxes(self):
        tax = 0
        for item in self.receipt:
            tax += item.price * 0.07
        return tax

    def calculate_total(self):
        total = 0
        for item in self.receipt:
            total += item.price
        return total + self.calculate_taxes()

    def print_receipt(self):
        print(f"The total due is {self.calculate_total():.3f}")
        print("CROSSROAD'S CAFE")
        print("----------------")

        for item in self.receipt:
            print(f"{item.name}: ${item.price:.2f}")

        print("----------------")
        print(f"taxes: ${self.calculate_taxes():.2f}")
        print("----------------")
        print(f"Total: ${self.calculate_total():.2f}")
