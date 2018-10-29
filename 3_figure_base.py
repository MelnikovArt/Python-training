# -*- coding: utf-8 -*-

"""
Анализ:
- Не понимаю, что объединить(какие методы, атрибуты) у классов фигур, для того
 чтобы применить наследование от общего класса Figure. Проблема, что все параметры
 и методы отличаются и будут переопределяться
- Как и зачем здесь класс Figure может выступить в роли родителя?
 (продолжение первого пункта)
- Не понимаю какой функционал должна выполнять программа, из-за этого
 ступр в организации кода. Описаны только структуры, нет предназначения.
"""


from math import pi, sqrt


def main():
	tr = Figure.create_triangle(5, 10, 5)
	tr_3d = Figure3D.create_triangle_3d(5, 10, 5, 10)
	# TODO logic
	return tr, tr_3d


class Figure(object):
	@staticmethod
	def create_triangle(a, b, c):
		return Triangle(a, b, c)

	@staticmethod
	def create_rectangle(a, b):
		return Rectangle(a, b)

	@staticmethod
	def create_circle(r):
		return Circle(r)

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
	# ASK Зачем наследоваться если всё переопределяем
	@staticmethod
	def create_triangle_3d(a, b, c, h):
		return Triangle3D(a, b, c, h)

	@staticmethod
	def create_rectangle_3d(a, b, h):
		return Rectangle3D(a, b, h)

	@staticmethod
	def create_circle_3d(r, h):
		return Circle3D(r, h)

	# ASK как правильно задать константу когда она зависит от импорта - блок try except?
	# ASK плохая практика задать константу как аргумент экз класса Circle?
	PI = pi


class Triangle3D(Triangle):
	def __init__(self, a, b, c, h):
		super(Triangle3D, self).__init__(a, b, c)
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


class Rectangle3D(Rectangle):
	def __init__(self, a, b, h):
		super(Rectangle3D, self).__init__(a, b)
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


class Circle3D(Circle):
	def __init__(self, r, h):
		super(Circle3D, self).__init__(r)
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
