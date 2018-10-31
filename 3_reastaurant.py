# -*- coding: utf-8 -*-

"""
Анализ

- Как называется этот паттерн проектирования?
- Не хватает проверок
"""


class Lunch(object):
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, food_name):
        self.customer.place_order(food_name, self.employee)

    def result(self):
        self.customer.print_food()


class Customer(object):
    def __init__(self):
        self.food = None

    def place_order(self, food_name, employee):
        food_obj = employee.take_order(food_name)
        self.food = food_obj.name

    def print_food(self):
        print self.food


class Employee(object):
    def take_order(self, food_name):
        food_obj = Food(food_name)
        return food_obj


class Food(object):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    today_lunch = Lunch()
    today_lunch.order('борщец')
    today_lunch.result()
