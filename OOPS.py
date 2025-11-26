import os

class OOPS:
    def __init__(self):
        self.name = "OOPS"
        self.version = "1.0"
        self.author = "John Doe"

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Version: {self.version}")
        print(f"Author: {self.author}")

class __main__():
    def __init__self():
        self.oops = OOPS()
        self.oops.display_info()

if __name__ == "main":
    __main__().__init__self()

class Vehicle:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed  

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Max Speed: {self.max_speed}")

    def __str__(self):
        return f"{self.name} - {self.max_speed}"

class Car(Vehicle):
    def __init__(self, name, max_speed, num_doors):
        super().__init__(name, max_speed)
        self.num_doors = num_doors  

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Max Speed: {self.max_speed}")
        print(f"Number of Doors: {self.num_doors}")

    def __str__(self):
        return f"{self.name} - {self.max_speed} - {self.num_doors}" 
    def __def__self():
        self.car = Car("Car",120,4)
        self.car.display_info()