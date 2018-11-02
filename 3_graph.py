# -*- coding: utf-8 -*-

"""
Варианты реализации:

ПЕРВЫЙ
- Создаем экземпляр Граф, имеет метод создания вершины (через создание экз Node).
- Объекты вершин хранятся в словаре экз Граф

- При создании вершины, ей определяется уникальное значение в аргумент 'key' (id вершины).
- Если вершина первая в графе, имеет ключ 'master'.
- Если вершина не первая и без связи с другой веошиной, ей определяется уникальное значение ключа.
- Если вершина создается со связью от другой вершины, то ей определяется связь через ключ *
* мысль про связь, сделать проще, set() ключей вершин, (который должен передаваться?)
- При создании связыннх вершин, между ними создается ребро (если правльно понимаю суть графов).
- TODO Орагинзовать у экз вершины хранение объектов ребер через словарь?

Далее реализовывать функции оперируя объектами. Вроде по смыслу подходит паттерн 'Построитель'.

ВТОРОЙ
- Через словари. Граф (объект словарь), содержит вершину (объект словарь) со списками: ребер
 (объект словарь) и вложенных вершин (объект словарь). Потом через рекусрию выполнять функции.
"""


class Graph(object):
    def __int__(self):
        self.nodes = {}

    def create_node(self, relate_node=None):
        if relate_node is None:
            new_node = Node(self)
        elif isinstance(relate_node, Node):
            new_node = Node(self, relate_node)

        self.nodes[new_node.key] = new_node

    def add_note(self):
        pass

    def del_note(self):
        pass

    # ASK как правильно давать имена параметрам с номерами, с логикой перечисления?
    def add_edge(self, node1, node2):
        pass

    def del_edge(self, node1, node2):
        pass

    def is_node(self, node_name):
        pass

    def iter_nodes(self):
        pass


class Node(object):
    def __init__(self, graph, relate_node):
        # TODO подумать, как создать связь через ключ
        self.key = 'master' if not graph.nodes else self._create_unique_key()
        self.edges = {}

    def get_related_nodes(self):
        # TODO сделать словарь у вершины и првоерять его?
        pass

    # TODO узнать как создать уникальное значение (через функцию?)
    def _create_unique_key(self):
        # TODO подумать по какой системе строиться связи между узлами, рассмотреть принцип криптографии + ноды
        pass


class Edge(object):
    def __init__(self, weight):
        self.weight = weight
        # TODO Алгоритм для определения начальной и конечной вершины
        self.primary_node = ''
        self.final_node = ''

    def get_native_nodes(self):
        pass

