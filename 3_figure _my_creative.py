# -*- coding: utf-8 -*-

"""
Анализ

- Решил дать смысл классу Figure и реализовал паттерн "Абстрактаня фабрика", но здесь он не подходит
(объект не состоит их дургих объектов) и реализация кривая в функции main.
- Сделал наследование от класса Figure для Figure3D, сократило код (не надо
повторять методы класса, сложное (вложенное) наследование в классах 3D фигур.
- Поработал с функцией супер.
- Попрактиковал декораторы classmethod

Результат, получилось сложно. Паттерн не к месту. Плюс только в отработке практики.
"""

from math import pi, sqrt


def main():
	t, r, c = create_figures(Figure)
	print t.search_corners()
	print r.is_square()
	print c.get_perimeter

	# t_3d, r_3d, c_3d = create_figures(Figure3D)
	# print t_3d.get_perimeter
	# print r_3d.is_square()
	# print c_3d.get_perimeter


def create_figures(factory):
	triangle = factory.create_triangle(5, 10, 5, 10)
	rectangle = factory.create_rectangle(10, 5, 10)
	circle = factory.create_circle(15, 10)
	return triangle, rectangle, circle


class Figure(object):
	# INFO Сначала сделал через передачу конкретных параметров,
	# но используя грппировку и расспаковку могу не переопределять методы дочернего класса (Figure3D)
	# ASK это плохая практика?
	@classmethod
	def create_triangle(cls, *args):
		return cls.Triangle(*args)

	@classmethod
	def create_rectangle(cls, *args):
		return cls.Rectangle(*args)

	@classmethod
	def create_circle(cls, *args):
		return cls.Circle(*args)

	# ASK как правильно задать константу когда она зависит от импорта - блок try except?
	# ASK плохая практика задать константу как аргумент экз класса Circle?
	PI = pi


	class Triangle(object):
		def __init__(self, a, b, c):
			self.a = a
			self.b = b
			self.c = c

		@property
		def get_perimeter(self):
			perimeter = self.a + self.b + self.c
			return perimeter

		@property
		def get_square(self):
			"""
			Use a Heron's formula
			"""
			p = 0.5 * (self.a + self.b + self.c)
			#  ASK или лучше через степень рассчитать квадратный корень, не трогая библиотеки?
			square = sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
			return square

		def search_corners(self):
			corner = 180
			return corner


	class Rectangle(object):
		def __init__(self, a, b):
			self.a = a
			self.b = b

		@property
		def get_perimeter(self):
			perimeter = 2 * (self.a + self.b)
			return perimeter

		@property
		def get_square(self):
			# Лишний расчет, решил использовать функции экз
			if self.is_square():
				square = self.a ** 2
				return square
			square = self.a + self.b
			return square

		def is_square(self):
			if self.a == self.b:
				return True
			return False


	class Circle(object):
		def __init__(self, r):
			self.r = r

		@property
		def get_perimeter(self):
			perimeter = 2 * Figure.PI * self.r
			return perimeter

		@property
		def get_square(self):
			square = Figure.PI * self.r * 2
			return square


class Figure3D(Figure):


	class Triangle(Figure.Triangle):
		def __init__(self, a, b, c, h):
			super(Figure3D.Triangle, self).__init__(a, b, c)
			self.h = h
			self.r = self.a / 2

		@property
		def get_volume(self):
			volume = (Figure3D.PI * self.r * self.h) / 3
			return volume

		@property
		def get_square(self):
			"""
			Use a Heron's formula
			"""

			square = Figure3D.PI * self.r * sqrt(self.r**2 + self.h**2)
			return square

		def search_corners(self):
			corner = 180
			return corner

	class Rectangle(Figure.Rectangle):
		def __init__(self, a, b, h):
			super(Figure3D.Rectangle, self).__init__(a, b)
			self.h = h

		@property
		def get_volume(self):
			if self.is_square():
				volume = self.a ** 3
				return volume
			volume = self.a * self.b * self.h
			return volume

		@property
		def get_square(self):
			# Лишний расчет, решил использовать функции экз
			if self.is_square():
				square = 6 * self.a**2
				return square
			square = 2 * (self.a*self.b + self.b*self.h + self.a*self.h)
			return square

		def is_square(self):
			if self.a == self.b == self.h:
				return True
			return False


	class Circle(Figure.Circle):
		def __init__(self, r, h):
			super(Figure3D.Circle, self).__init__(r)
			self.h = h

		@property
		def get_volume(self):
			volume = (4 * Figure3D.PI * self.r**3) / 3
			return volume

		@property
		def get_square(self):
			square = 4 * Figure3D.PI * self.r**2
			return square


if __name__ == '__main__':
	main()


# TODO округлить результаты значений параметров и площадей
