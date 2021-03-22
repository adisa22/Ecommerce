class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
           if inventory_dict[product] > 0:
               self.purchases.append(product)
               inventory_dict[product] -= 1
           else:
               print('We are out of stock!')
        else:
            print("We don't have that product!")

    def print_purchases(self):
        print("The customer has purchased")
        for item in self.purchases:
            print(item.name)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product]= quantity
        else:
            self.inventory[product] += quantity

    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key.name + ':' + str(value))
            print()

customer = Customer('Karen', 'Karen62@aol.com')
#print(customer.name)
#print(customer.email)

IPhone = Product('IPhoneXr', 650)
#print(IPhone.name)
#print(IPhone.price)

Mac = Product("Mac",2000)
#print(Mac.name)
#print(Mac.price)

inventory = Inventory()
inventory.add_product(IPhone, 400)
#inventory.print_inventory()
inventory.add_product(Mac, 420)

inventory.print_inventory()
customer.purchase (inventory, IPhone)
customer.purchase(inventory, Mac)
inventory.print_inventory()
customer.print_purchases()




    

