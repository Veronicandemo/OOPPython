class Car:
    wheels = 4
    def __init__(self, make,model,color):
        self.make = make
        self.model = model
        self.color = color
        self.speed = 0
    def hooting(self):
        return 'beep beep'
    def accelerate(self):
        self.speed = kmh
        return f'Accelerationg to {self.speed} km/h '
    def stop(self):
        this.speed = 0
        return f"the car's speed is at {self.speed}"