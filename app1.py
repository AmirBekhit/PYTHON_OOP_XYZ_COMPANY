#!/usr/bin/env Python3

"""
app.py - XYZ, Tokyo - JAPAN
This program allows me to manage my employees.
@author:Amir Bekhit 
@version2.0 - 06.03.2020
"""


class Employee(object):
    # Constructor Method
    def __init__(self, theName, thePhone, theEmail):
        self.name = theName
        self.phone = thePhone
        self.email = theEmail

    # Accessor Method (Getters)
    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    # Mutator Method (Setters)
    def setPhone(self, newPhoneNumber):
        self.phone = newPhoneNumber

    def setEmail(self, newEmail):
        self.email = newEmail

    def __str__(self):
        return "Employee [name: " + self.name + \
            " ,Phone:" + self.phone + \
            " ,Email: " + self.email + '].'

    # def __repr__(self):
    #     return '{self.__class__.__name__}({self.name} , {self.phone} , {self.email})'.format(self=self)


def enter_employee():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    return Employee(name, phone, email)


def lookup_employee(employees):
    found = False
    key = input("Enter key to lookup:")
    for employee in employees:
        if key in employee.getName():
            print(employee)
            found = True
        elif key in employee.getPhone():
            print(employee)
            found = True
        elif key in employee.getEmail():
            print(employee)
            found = True
    if not found:
        print("No Employees match that term")


def show_all_employees(employees):
    print('Showing all employees...')
    for employee in employees:
        print(employee)


def main():
    employees = []
    running = True
    while running:
        print("* X.Y.Z Company, Tokyo JAPAN *")
        print("* Employees contacts Manager *")
        print("1) new employee      2)lookup")
        print("3) show all          4)quit")
        option = input("> ")
        if option == "1":
            employees.append(enter_employee())
        elif option == "2":
            lookup_employee(employees)
        elif option == "3":
            show_all_employees(employees)
        elif option == "4":
            running = False
        else:
            print('Error! unrecognized input. Please Try Again.')
    print('program terminated!')


if __name__ == "__main__":
    main()
