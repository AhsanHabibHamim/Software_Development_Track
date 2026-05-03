# Customer
# Employe
# Admin
from abc import ABC


class User(ABC):

    def __init__(self, name, email, address, phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone


class Employee(User):
    def __init__(self, name, email, address, phone, age, designation, salary):
        super().__init__(name, email, address, phone)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, email, address, phone):
        super().__init__(name, email, address, phone)
        self.employees = []  # Working as a database

    def add_employee(self, Restuarent, employee):
        Restuarent.add_employee(employee)

    def view_employee(self, Restuarent):
        Restuarent.view_employee()

    def add_item(self, Restuarent, item):
        Restuarent.menu.add_menu_item(item)

    def remove_item(self, Restuarent, item):
        Restuarent.menu.remove_item(item)


class Restuarent:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Working as a database
        self.menu = FoodItem()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("Employee List")
        for emp in self.employees:
            print(emp.name, emp.email, emp.address, emp.phone, emp.age)


class Menu:
    def __init__(self):
        self.items = []  # items er database

    def add_menu_item(self, item):
        self.items.append(item)

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Deleted")

        else:
            print("Items Not Found")

    def show_item(self):
        print("***Menue Item***")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")


class FoodItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity



