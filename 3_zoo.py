# -*- coding: utf-8 -*-

"""
Анализ:

- В методах класса Zoo добавленя животных дублируется логика определения какой класс создавать,
нужно сделать приватный метод для Zoo.
- По правильному нужно в методе add_animal_with_console (класс Zoo) делать првоерку каждого
входного значения (пустой, верный тип данных, ограничения по сиволам, валидность), через цикл while
повторять запрос пока условия не выполнятся, это очень много кода (try except, if, while) нужно делать?
- По итогу работы метода add_animal_with_file (class Zoo) нужно проводить проверку наличия None значения
в списке self.animals
"""

import os


class Zoo(object):
    def __init__(self, *args):
        self.animals = []

        for animal in args:
            if isinstance(animal, Animal):
                self.animals.append(animal)

    # ASK Правильно понял подзадачу №5 решать через raw_input или argparse?
    def add_animal_with_console(self):
        # TODO добавить обработку ошибок
        name = raw_input('Animal Name?')
        type_ = raw_input('Animal Type?')
        specification = raw_input('Animal Species?')
        weight = int(raw_input('Animal Weight?'))
        img = raw_input('Animal Image?')
        voice = raw_input('Animal Sound?')

        if type_.lower() == 'bird':
            wingspan = int(raw_input('Animal Wingspan?'))
            is_talk = bool(raw_input('Animal is Talking?'))  # TODO Изменить определние булевого значения
            if is_talk:
                phrase = raw_input('Animal Phrase?')
            animal = Bird(name, type_, specification, weight, img, voice, wingspan, is_talk, phrase)
        elif type_.lower() == 'mammal':
            litter_size = int(raw_input('Animal Litter Size?'))
            animal = Mammal(name, type_, specification, weight, img, voice, litter_size)
        elif type_.lower() == 'reptile':
            is_venomous = bool(raw_input('Animal is Venomous?'))
            animal = Reptile(name, type_, specification, weight, img, voice, is_venomous)

        self.animals.append(animal)

    def add_animal_with_file(self, file_name):
        """
        Add animal from file
        :param file_name: must have text a strong structure,
        values separate each other with comma? example - 'text,text'
        :return: None
        """
        if not os.path.isfile(file_name):
            print 'File does\'t exist'
            # ASK Если по логике не закладывать повторный ввод значения.
            # Как привильно выйти из метода, если условие не выполняется, через return?
            return
        if os.stat(file_name).st_size == 0:
            print 'File is empty'
            return

        count = 0

        with open(file_name) as f:
            for line in f.readlines():
                new_animal = None
                animal = line.strip().split(',')
                print animal

                if len(animal) < 7 or animal is None:
                    continue

                if animal[1].lower() == 'bird':  # type animal
                    if len(animal) != 8 and len(animal) != 9:
                        continue
                    new_animal = Bird(*animal)
                elif animal[1].lower() == 'mammal':  # type animal
                    if len(animal) != 7:
                        continue
                    new_animal = Mammal(*animal)
                elif animal[1].lower() == 'reptile':  # type animal
                    if len(animal) != 7:
                        continue
                    new_animal = Reptile(*animal)

                self.animals.append(new_animal)
                count += 1

        print 'Added %s animal%s' % (count, '' if count == 1 else 's')

    def search_animal(self, name):
        for animal in self.animals:
            name_mod = name.lower()
            if name_mod == animal.name:
                print '%s есть в зоопарке' % (name)
                return
        print '%s нет в зоопарке' % (name)

    def get_animal_atr(self):
        animal_args = {
            's': 'specification',
            'm': 'weight',
            'l': 'litter_size',  # mammal
            'v': 'is_venomous',  # reptile
            'w': 'wingspan',  # bird
            't': 'is_talk',  # bird

        }

        arg = raw_input('Query animal species[s], mass[m], litter[l], '
                        'venom[v], wingspan[w], talk[t] or exit session[e]? ')
        animal_name = raw_input('Animal Name? ')

        for animal in self.animals:
            if animal_name.lower() == animal.name:
                if animal_args[arg] in animal.__dict__:
                    print '%s %s is %s' % (animal.name.capitalize(),
                                           animal_args[arg],
                                           animal.__getattribute__(animal_args[arg]))
                print '%s doesn\'t attribute - %s' % (animal_name, animal_args[arg])


class Animal(object):
    def __init__(self, name, type_, specification, weight, img, voice):
        # ASK хорошая практика данные типа str приводит к одному формату (все символы строчные)?
        self.name = name.lower()
        self.type = type_.lower()
        self.specification = specification.lower()
        self.weight = weight
        # ASK Где проверять валидность входных данных (атрибутов)?
        # нужно поместить атрибут self.img и self.voice в блок try except или в условия для
        # проверки, что картинка это путь к файлу, файл is картинка и др? (тоже самое для голоса)
        self.img = img
        self.voice = voice

    @property
    def get_name(self):
        return self.name

    @property
    def get_img(self):
        try:
            # ASK целесообразно импорт разместить внутри функции, где используется библиотека?
            from PIL import Image

            img = Image.open(self.img)
            return img.show()
        except ImportError as err:
            print err.message

    @property
    def get_voice(self):
        try:
            from winsound import PlaySound, SND_FILENAME

            voice = PlaySound(self.voice, SND_FILENAME)
            return voice
        except ImportError as err:
            print err.message


class Bird(Animal):
    def __init__(self, name, type_, specification,
                 weight, img, voice, wingspan, is_talk, phrase=None):
        super(Bird, self).__init__(name, type_, specification,
                                   weight, img, voice)
        self.wingspan = wingspan if wingspan > 1 else 1
        self.is_talk = is_talk
        if is_talk:
            self.phrase = phrase


class Mammal(Animal):
    def __init__(self, name, type_, specification,
                 weight, img, voice, litter_size):
        super(Mammal, self).__init__(name, type_, specification,
                                     weight, img, voice)
        self.litter_size = litter_size if litter_size > 1 else 1


class Reptile(Animal):
    def __init__(self, name, type_, specification,
                 weight, img, voice, is_venomous):
        super(Reptile, self).__init__(name, type_, specification,
                                      weight, img, voice)
        self.is_venomous = is_venomous


if __name__ == '__main__':
    # ПУНКТ - 3
    a = Bird('Sparrow', 'Bird', 'Feather', 100,
             'sparrow.jpg', 'sparrow.mp3', 20, False)
    # ASK Правильно под каждый параметр создавать функцию get_atr, а не выводить обращаясь на прямую?
    print a.get_name, a.type, a.specification, a.weight, \
        '(%s, %s, %s, %s)' % (a.img, a.voice, a.wingspan, a.is_talk)

    # ПУНКТ - 4
    new_bird = Bird('Eagle', 'Bird', 'Feather', 100,
                     'sparrow.jpg', 'sparrow.mp3', 20, False)

    moscow_zoo = Zoo(a, new_bird)
    # ПУНКТ - 5
    moscow_zoo.add_animal_with_console()
    # ПУНКТ - 6
    moscow_zoo.add_animal_with_file('list of animals')
    # ПУНКТ - 7
    moscow_zoo.search_animal('SparRow')
    # ПУНКТ - 8
    moscow_zoo.get_animal_atr()
