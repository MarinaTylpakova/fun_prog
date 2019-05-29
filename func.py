from collections.abc import Iterable
from collections import OrderedDict
from itertools import groupby


# 1. Написать функцию получения размера генератора

def ilen(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> ilen(foo)
    10
    """
    return sum(1 for item in iterable)


# 3. Написать функцию, которая удалит дубликаты, сохранив порядок

def distinct(iterable: Iterable):
    """
    >>> list(distinct([1, 2, 0, 1, 3, 0, 2]))
    [1, 2, 0, 3]
    """
    return OrderedDict.fromkeys(iterable)


# 5. Написать функцию, которая разобьет последовательность на заданные куски

def chunks(size: int, iterable: Iterable):
    """
    >>> list(chunks(3, [0, 1, 2, 3, 4]))
    [(0, 1, 3), (4, )]
    """
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


# 6. Написать функцию получения первого элемента или None

def first(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> first(foo)
    0
    >>> first(range(0))
    None
    """
    for element in iterable:
        if element:
            return element
        else:
            return None
