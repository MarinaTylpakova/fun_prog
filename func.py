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


# 2. Написать функцию flatten, которая из многоуровневого массива сделает одноуровневый

class chain():

    def from_iterable(iterables):
        # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
        for it in iterables:
            for element in it:
                if isinstance(element, list):
                    for ii in element:
                        yield from flatten(element)
                        break
                else:
                    yield element


def flatten(iterable: Iterable):
    """
    >>> list(flatten([0, [1, [2, 3]]]))
    [0, 1, 2, 3]


    >>> list(flatten(['0', ['1', ['2', ['7',['4', '3'],'8'], '3']]]))
    ['0', '1', '2', '7', '4', '3', '8', '3']
    """

    return chain.from_iterable(iterable)


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
        
        
 # 7. Написать функцию получения последнего элемента или None

def last(iterable: Iterable):
    """
    >>> foo = (x for x in range(10))
    >>> last(foo)
    9
    >>> last(range(0))
    None
    """
    last_elem = None
    for element in iterable:
        last_elem = element
    return last_elem



# 8. Написать функцию слайсинга (без step)

def islice(iterable: Iterable, start, stop):
    """
    >>> foo = (x for x in range(10))
    >>> islice(foo, None, 3)
    [0, 1, 2]
    >>> islice(foo, -3, None)
    [7, 8, 9]
    """
    result = []
    res = []

    for i in iterable:
        result.append(i)

    if start == None:
        start = 0
    elif stop == None:
        stop = len(result)

    it = iter(range(start, stop))
    nexti = next(it)
    res.append(nexti)
    for i, element in enumerate(result):
        if i == nexti:
            yield element
            nexti = next(it)
            res.append(element)
    return res

