class Fruit:
    quantity = 0
    def __init__(self, price,name,color):
        self.price = price
        self.name = name
        self.color = color
    def add_fruits(self, quant):
        self.quantity += quant
        return f'There are now {self.quantity} {self.name}'
    def remove_fruits(self, quant):
        self.quantity -= quant
        return f'The fruits have reduced to {self.quantity} {self.name}'
    def eat_fruit(self):
        return f"Have a {fruit.name} and enjoy the tastee"