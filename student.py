import datetime

year = datetime.date.today().year

# Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials
class Student:
    # Class variables
    school = 'AkiraChix'
    def __init__(self, first_name,last_name,age, country):
        # Instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.age =  age
        self.country = country
    def show_full_name(self):
        return f'{self.first_name} {self.last_name}'
    def year_of_birth(self):
        return year - self.age
    def show_initials(self):
        return f'{self.first_name[0]}.{self.last_name[0]}'
    
    # def greet_student(self):
    #     return f'Hello {self.name}, Welcome to {self.school}'
    # def year_of_birth(self):
    #     year =  2023 - self.age
    #     return f'Hello {self.name} you were born in the year {self.year}'

#  Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account