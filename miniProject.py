from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    @abstractmethod
    def category(self):
        pass

class Book(Product):
    def category(self):
        return "Book"

class Laptop(Product):
    def category(self):
        return "Laptop"


class ProductFactory:
    @staticmethod
    def create(t, name, price, stock):
        if t == "book":
            return Book(name, price, stock)
        if t == "laptop":
            return Laptop(name, price, stock)
        raise ValueError("Unknown product type")

class Inventory:
    def __init__(self):
        self.items = []

    def add(self, product):
        self.items.append(product)

    def list(self):
        for p in self.items:
            print(p.name, p.category(), p.price, p.stock)