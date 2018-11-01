# -*- coding: utf-8 -*-

"""
Анализ:

- Не стал реализовывать полноценную логику каждого метода по переводу
чисел из одной системы в другую т.к. понимаю цель задания в создании
классов и организация их структуры, понимания наследования, спец методов.
- Узнал, что такое абстрактные классы и методы, как их создавать
- Поразбирался в системах счисления, рассмотрел варианты как узнать тип
данных СС, с функциями преобразующими СС и их возвращаемыми значениями.
- Познакомился с новыми специальными методами в python 2
- Страшная реализация метода _convert класса ConvertFull, вижу выход:
создать отдельный метод по преобразованию числа из разных СС в int,
второе создать словарь с ключами названий СС и сценариями преобразования
(додумать надо)
- Зачем pyCharm предлагает каждый вторый метод сделать статическим, в
чем преимущство?
- По 5 заданию, понял, что исказил реализцаию. Класс должен иметь 1
аргумент (число в какой-то СС), который переопределяется методами класса
- TODO Пункты #5 и №6 реализовал не полноценно(без определения СС числа)
- TODO изучить инструмент functools.total_ordering()(в рамках пункта №6)
"""

from abc import ABCMeta, abstractmethod


class ExecutableClass(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __call__(self):
        pass


class Convert(ExecutableClass):
    def __init__(self, dec_number):
        self.dec_number = self._valid_input(dec_number)  # type -> int
        self.rom_number = self._convert_dec_to_rom(self.dec_number)

    def __call__(self):
        print self.rom_number

    def __add__(self, other):
        return self.dec_number + other.dec_number

    def __sub__(self, other):
        return self.dec_number - other.dec_number

    def __mul__(self, other):
        return self.dec_number * other.dec_number

    def __div__(self, other):
        return self.dec_number / other.dec_number

    def __eq__(self, other):
        return self.dec_number == other.dec_number

    def __ne__(self, other):
        return self.dec_number != other.dec_number

    # def __lt__(self, other):
    #     return self.dec_number < other.dec_number

    def __gt__(self, other):
        return self.dec_number > other.dec_number

    def __le__(self, other):
        return self.dec_number <= other.dec_number

    def __ge__(self, other):
        return self.dec_number >= other.dec_number

    def _convert_dec_to_rom(self, value):
        if value:
            # TODO Логику перевода десятичного числа в римское
            return 'X' * len(str(value))

    # ASK Вижу не сколько способов проверки входного ключевого значения:
        # 1 - Как реализовано сейчас
        # 2 - Присвоить входное значение атрибуту экземпляра, затем проверять его перед
            # использованием в методах.
        # 3 - Делать отдельный модуль с функциями валидности и других првоерок, при
            # определении экз сначала отрабатывают проверочный модуль, как правльно для этой задачи?
    def _valid_input(self, value):
        # TODO Разные проверки - input is decimal system
        if value:
            return value
        print 'Ввели число не из десятичной системы счисления'
        return None


class ConvertPlus(Convert):
    def __init__(self, dec_number):
        super(ConvertPlus, self).__init__(dec_number)

    def __call__(self):
        print self._convert_rom_to_dec()

    def _convert_rom_to_dec(self):
        # TODO логику обратной конвертации
        return self.dec_number


class ConvertFull(ConvertPlus):
    def __init__(self, dec_number):
        super(ConvertFull, self).__init__(dec_number)
        self.bin_number = self._convert(self.dec_number, 'bin')
        self.oct_number = self._convert(self.dec_number, 'oct')
        self.hex_number = self._convert(self.dec_number, 'hex')

    def __call__(self):
        print self._convert(self.dec_number, 'bin')

    def _convert(self, value, conv_num_system):
        # TODO Нужен хелпер по допустимым значениям con_num_system и проверка корректного input значения
        num_system_value = self._indicate_number_system(value)

        if conv_num_system == 'rom':
            if num_system_value == 'int':
                value_int = value
            elif num_system_value == 'bin':
                value_int = int(value, 2)
            elif num_system_value == 'oct':
                value_int = int(value, 8)
            elif num_system_value == 'hex':
                value_int = int(value, 16)
            res = self._convert_dec_to_rom(value_int)
            # return res

        elif conv_num_system == 'int':
            if num_system_value == 'rom':
                res = self._convert_rom_to_dec(value)
            elif num_system_value == 'bin':
                res = bin(value)
            elif num_system_value == 'oct':
                res = oct(value)
            elif num_system_value == 'hex':
                res = hex(value)
            # return res

        elif conv_num_system == 'bin':
            if num_system_value == 'int':
                res = bin(value)
            else:
                value_int = int(value, 2)
                if num_system_value == 'rom':
                    res = self._convert_dec_to_rom(value_int)
                elif num_system_value == 'oct':
                    res = oct(value_int)
                elif num_system_value == 'hex':
                    res = hex(value_int)
            # return res

        elif conv_num_system == 'oct':
            if num_system_value == 'int':
                res = oct(value)
            else:
                value_int = int(value, 8)
                if num_system_value == 'rom':
                    res = self._convert_dec_to_rom(value_int)
                elif num_system_value == 'bin':
                    res = bin(value_int)
                elif num_system_value == 'hex':
                    res = hex(value_int)
        # return res

        elif conv_num_system == 'hex':
            if num_system_value == 'int':
                res = hex(value)
            else:
                value_int = int(value, 16)
                if num_system_value == 'rom':
                    res = self._convert_dec_to_rom(value_int)
                elif num_system_value == 'bin':
                    res = bin(value_int)
                elif num_system_value == 'oct':
                    res = oct(value_int)
        # return res

        # ASK в такой вложенной системе условий, вовращать значение
            # правильно одним return после всех условий или после
            # каждой ветки указывать (закомментированны)
        return res

    def _indicate_number_system(self, value):
        # ASK Как грамотно определить систему счисления?
        if isinstance(value, int):
            return 'int'
        elif isinstance(value, basestring):
            if value.startswith('0b'):
                return 'bin'
            elif value.startswith('0x'):
                return 'hex'
            elif value.startswith('0'):
                return 'oct'
            else:
                return 'rom'

    # TODO Метод конверктации значения value into int


if __name__ == '__main__':
    a = Convert(112)
    # a()

    b = Convert(888)
    # print a + b
    print a == b
    print a != b
    print a < b  # ASK Почему работает если я закоментировал спец метод? (62 строка)
    print a > b
    print a <= b
    print a >= b

    # c = ConvertFull(12345)
    # print c.dec_number
    # print c.rom_number
    # print c.bin_number
    # print c.oct_number
    # print c.hex_number
    # c()
