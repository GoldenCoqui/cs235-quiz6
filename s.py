class OrderDetails:
    def __init__(self, customer_info, items, shipping_address):
        self.customer_info = customer_info
        self.items = items
        self.shipping_address = shipping_address

    def display_order_details(self):
        print("Order Details:")
        print("Customer Info:", self.customer_info)
        print("Items:", self.items)
        print("Shipping Address:", self.shipping_address)


class OrderCostCalculator:
    def calculate_total_order_cost(self, items):
        total_cost = sum(item['price'] for item in items)
        print("Total Order Cost:", total_cost)


class OrderValidator:
    def validate_order_data(self, items, shipping_address):
        # Dummy validation
        if not items or not shipping_address:
            print("Invalid order data! Items or shipping address missing.")
        else:
            print("Order data is valid.")


class OrderEmailSender:
    def send_order_confirmation_email(self, customer_email):
        # Dummy email sending
        print("Order confirmation email sent to:", customer_email)


class InventoryUpdater:
    def update_inventory(self, items):
        # Dummy inventory update
        print("Inventory updated after processing the order.")


def main():
    # Dummy values
    customer_info = "John Doe"
    items = [{'name': 'Item1', 'price': 20}, {'name': 'Item2', 'price': 30}]
    shipping_address = "123 Main St, City"
    customer_email = "john@example.com"

    # Creating instances of each class
    order_details = OrderDetails(customer_info, items, shipping_address)
    order_cost_calculator = OrderCostCalculator()
    order_validator = OrderValidator()
    order_email_sender = OrderEmailSender()
    inventory_updater = InventoryUpdater()

    # Performing actions
    order_details.display_order_details()
    order_cost_calculator.calculate_total_order_cost(items)
    order_validator.validate_order_data(items, shipping_address)
    order_email_sender.send_order_confirmation_email(customer_email)
    inventory_updater.update_inventory(items)


if __name__ == "__main__":
    main()
