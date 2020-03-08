#!/usr/bin/env Python3

"""
app.py - XYZ, Tokyo - JAPAN
This program allows me to manage my employees.
@author:Amir Bekhit 
@version1.0 - 06.03.2020
"""


def main():

    employees = []

    for i in range(2):
        print('employee information')
        name = input('Enter Name : ')
        empId = input('Enter ID: ')
        department = input('Enter department: ')
        employees.append([name, empId, department])

    for x in range(len(employees)):
        print('Company Employee')
        for y in range(len(employees[x])):
            print(employees[x][y])


if __name__ == "__main__":
    main()
