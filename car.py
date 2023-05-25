class Car:
    wheels = 4
    def __init__(self, make,model,color):
        self.make = make
        self.model = model
        self.color = color
        self.speed = 0
        self.name = ''     
    def hooting(self):
        return 'beep beep'
    def accelerate(self, acc):
        self.speed += acc
        return f'Accelerating to {self.speed} km/h '
    def stop(self):
        self.speed = 0
        return f"the car's speed is at {self.speed}"
car2 = Car('Toyota', 'toyota', 'blue')
# car2.name = 'jeep'
car2.wheels = 5
print(car2.wheels)
print(car2.name)
# print(car2.name = 'jeep')
from datetime import datetime, timedelta
print("Current time: ", datetime.now())
print(datetime.now() + timedelta(days=2))