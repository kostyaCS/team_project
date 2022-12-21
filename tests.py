"""
This module tests all function that are in main.py
"""
from main import count, cycle, repeat, combinations,\
 combinations_with_replacement, permutations, product


def count_test():
    """
    Function for testing count from main
    """
    counter_object = count(10)
    assert next(counter_object) == 10
    assert next(counter_object) == 11
    assert next(counter_object) == 12

    counter_object = count(5, 3)
    assert next(counter_object) == 5
    assert next(counter_object) == 8
    assert next(counter_object) == 11

    counter_object = count(100, -10)
    assert next(counter_object) == 100
    assert next(counter_object) == 90
    assert next(counter_object) == 80


def cycle_test():
    """
    Function for testing cycle from main
    """
    cycle_object = cycle([1, 2, 3, 4, 5])
    assert next(cycle_object) == 1
    assert next(cycle_object) == 2
    assert next(cycle_object) == 3
    assert next(cycle_object) == 4
    assert next(cycle_object) == 5
    assert next(cycle_object) == 1


def repeat_test():
    """
    Function for testing repeat from main
    """
    repeat_object = repeat('abc')
    assert next(repeat_object) == 'abc'
    assert next(repeat_object) == 'abc'
    assert next(repeat_object) == 'abc'
    assert next(repeat_object) == 'abc'

    repeat_object = repeat(None)
    assert next(repeat_object) is None
    assert next(repeat_object) is None


def combinations_test():
    """
    Function for testing combinations from main
    """
    assert list(combinations('University', 3)) == [('U', 'n', 'i'), ('U', 'n', 'v'),
    ('U', 'n', 'e'), ('U', 'n', 'r'), ('U', 'n', 's'), ('U', 'n', 'i'), ('U', 'n', 't'),
    ('U', 'n', 'y'), ('U', 'i', 'v'), ('U', 'i', 'e'), ('U', 'i', 'r'), ('U', 'i', 's'),
    ('U', 'i', 'i'), ('U', 'i', 't'), ('U', 'i', 'y'), ('U', 'v', 'e'), ('U', 'v', 'r'),
    ('U', 'v', 's'), ('U', 'v', 'i'), ('U', 'v', 't'), ('U', 'v', 'y'), ('U', 'e', 'r'),
    ('U', 'e', 's'), ('U', 'e', 'i'), ('U', 'e', 't'), ('U', 'e', 'y'), ('U', 'r', 's'),
    ('U', 'r', 'i'), ('U', 'r', 't'), ('U', 'r', 'y'), ('U', 's', 'i'), ('U', 's', 't'),
    ('U', 's', 'y'), ('U', 'i', 't'), ('U', 'i', 'y'), ('U', 't', 'y'), ('n', 'i', 'v'),
    ('n', 'i', 'e'), ('n', 'i', 'r'), ('n', 'i', 's'), ('n', 'i', 'i'), ('n', 'i', 't'),
    ('n', 'i', 'y'), ('n', 'v', 'e'), ('n', 'v', 'r'), ('n', 'v', 's'), ('n', 'v', 'i'),
    ('n', 'v', 't'), ('n', 'v', 'y'), ('n', 'e', 'r'), ('n', 'e', 's'), ('n', 'e', 'i'),
    ('n', 'e', 't'), ('n', 'e', 'y'), ('n', 'r', 's'), ('n', 'r', 'i'), ('n', 'r', 't'),
    ('n', 'r', 'y'), ('n', 's', 'i'), ('n', 's', 't'), ('n', 's', 'y'), ('n', 'i', 't'),
    ('n', 'i', 'y'), ('n', 't', 'y'), ('i', 'v', 'e'), ('i', 'v', 'r'), ('i', 'v', 's'),
    ('i', 'v', 'i'), ('i', 'v', 't'), ('i', 'v', 'y'), ('i', 'e', 'r'), ('i', 'e', 's'),
    ('i', 'e', 'i'), ('i', 'e', 't'), ('i', 'e', 'y'), ('i', 'r', 's'), ('i', 'r', 'i'),
    ('i', 'r', 't'), ('i', 'r', 'y'), ('i', 's', 'i'), ('i', 's', 't'), ('i', 's', 'y'),
    ('i', 'i', 't'), ('i', 'i', 'y'), ('i', 't', 'y'), ('v', 'e', 'r'), ('v', 'e', 's'),
    ('v', 'e', 'i'), ('v', 'e', 't'), ('v', 'e', 'y'), ('v', 'r', 's'), ('v', 'r', 'i'),
    ('v', 'r', 't'), ('v', 'r', 'y'), ('v', 's', 'i'), ('v', 's', 't'), ('v', 's', 'y'),
    ('v', 'i', 't'), ('v', 'i', 'y'), ('v', 't', 'y'), ('e', 'r', 's'), ('e', 'r', 'i'),
    ('e', 'r', 't'), ('e', 'r', 'y'), ('e', 's', 'i'), ('e', 's', 't'), ('e', 's', 'y'),
    ('e', 'i', 't'), ('e', 'i', 'y'), ('e', 't', 'y'), ('r', 's', 'i'), ('r', 's', 't'),
    ('r', 's', 'y'), ('r', 'i', 't'), ('r', 'i', 'y'), ('r', 't', 'y'), ('s', 'i', 't'),
    ('s', 'i', 'y'), ('s', 't', 'y'), ('i', 't', 'y')]

    combinations_object = combinations('ABABAGALAMAGA', 7)
    assert next(combinations_object) == ('A', 'B', 'A', 'B', 'A', 'G', 'A')
    assert next(combinations_object) == ('A', 'B', 'A', 'B', 'A', 'G', 'L')
    assert next(combinations_object) == ('A', 'B', 'A', 'B', 'A', 'G', 'A')
    assert next(combinations_object) == ('A', 'B', 'A', 'B', 'A', 'G', 'M')


def combinations_with_replacement_test():
    """
    Function for testing combinations_with_replacement from main
    """
    combinations_with_replacement_object = combinations_with_replacement('ABC', 2)
    assert next(combinations_with_replacement_object) == ('A', 'A')
    assert next(combinations_with_replacement_object) == ('A', 'B')
    assert next(combinations_with_replacement_object) == ('A', 'C')
    assert next(combinations_with_replacement_object) == ('B', 'B')
    assert next(combinations_with_replacement_object) == ('B', 'C')

    assert list(combinations_with_replacement([53, 6543, 12, 786], 3)) == [(53, 53, 53),
     (53, 53, 6543), (53, 53, 12), (53, 53, 786), (53, 6543, 6543), (53, 6543, 12),
      (53, 6543, 786), (53, 12, 12), (53, 12, 786), (53, 786, 786), (6543, 6543, 6543),
       (6543, 6543, 12), (6543, 6543, 786), (6543, 12, 12), (6543, 12, 786),
        (6543, 786, 786), (12, 12, 12), (12, 12, 786), (12, 786, 786), (786, 786, 786)]
    assert tuple(combinations_with_replacement(('a', 'b', 'd', 'u'), 4)) == (('a', 'a', 'a', 'a'),
            ('a', 'a', 'a', 'b'), ('a', 'a', 'a', 'd'), ('a', 'a', 'a', 'u'), ('a', 'a', 'b', 'b'),
            ('a', 'a', 'b', 'd'), ('a', 'a', 'b', 'u'), ('a', 'a', 'd', 'd'), ('a', 'a', 'd', 'u'),
            ('a', 'a', 'u', 'u'), ('a', 'b', 'b', 'b'), ('a', 'b', 'b', 'd'), ('a', 'b', 'b', 'u'),
            ('a', 'b', 'd', 'd'), ('a', 'b', 'd', 'u'), ('a', 'b', 'u', 'u'), ('a', 'd', 'd', 'd'),
            ('a', 'd', 'd', 'u'), ('a', 'd', 'u', 'u'), ('a', 'u', 'u', 'u'), ('b', 'b', 'b', 'b'),
            ('b', 'b', 'b', 'd'), ('b', 'b', 'b', 'u'), ('b', 'b', 'd', 'd'), ('b', 'b', 'd', 'u'),
            ('b', 'b', 'u', 'u'), ('b', 'd', 'd', 'd'), ('b', 'd', 'd', 'u'), ('b', 'd', 'u', 'u'),
            ('b', 'u', 'u', 'u'), ('d', 'd', 'd', 'd'), ('d', 'd', 'd', 'u'), ('d', 'd', 'u', 'u'),
            ('d', 'u', 'u', 'u'), ('u', 'u', 'u', 'u'))
    assert list(combinations_with_replacement([], 2)) == list()


def permutations_test():
    """
    Function for testing permutations from main
    """
    permutations_object = permutations([1, 2, 3])
    assert next(permutations_object) == (1, 2, 3)
    assert next(permutations_object) == (1, 3, 2)
    assert next(permutations_object) == (2, 1, 3)
    assert next(permutations_object) == (2, 3, 1)
    assert next(permutations_object) == (3, 1, 2)
    assert next(permutations_object) == (3, 2, 1)

    assert list(permutations('abcde')) == [('a', 'b', 'c', 'd', 'e'), ('a', 'b', 'c', 'e', 'd'),
        ('a', 'b', 'd', 'c', 'e'), ('a', 'b', 'd', 'e', 'c'), ('a', 'b', 'e', 'c', 'd'),
        ('a', 'b', 'e', 'd', 'c'), ('a', 'c', 'b', 'd', 'e'), ('a', 'c', 'b', 'e', 'd'),
        ('a', 'c', 'd', 'b', 'e'), ('a', 'c', 'd', 'e', 'b'), ('a', 'c', 'e', 'b', 'd'),
        ('a', 'c', 'e', 'd', 'b'), ('a', 'd', 'b', 'c', 'e'), ('a', 'd', 'b', 'e', 'c'),
        ('a', 'd', 'c', 'b', 'e'), ('a', 'd', 'c', 'e', 'b'), ('a', 'd', 'e', 'b', 'c'),
        ('a', 'd', 'e', 'c', 'b'), ('a', 'e', 'b', 'c', 'd'), ('a', 'e', 'b', 'd', 'c'),
        ('a', 'e', 'c', 'b', 'd'), ('a', 'e', 'c', 'd', 'b'), ('a', 'e', 'd', 'b', 'c'),
        ('a', 'e', 'd', 'c', 'b'), ('b', 'a', 'c', 'd', 'e'), ('b', 'a', 'c', 'e', 'd'),
        ('b', 'a', 'd', 'c', 'e'), ('b', 'a', 'd', 'e', 'c'), ('b', 'a', 'e', 'c', 'd'),
        ('b', 'a', 'e', 'd', 'c'), ('b', 'c', 'a', 'd', 'e'), ('b', 'c', 'a', 'e', 'd'),
        ('b', 'c', 'd', 'a', 'e'), ('b', 'c', 'd', 'e', 'a'), ('b', 'c', 'e', 'a', 'd'),
        ('b', 'c', 'e', 'd', 'a'), ('b', 'd', 'a', 'c', 'e'), ('b', 'd', 'a', 'e', 'c'),
        ('b', 'd', 'c', 'a', 'e'), ('b', 'd', 'c', 'e', 'a'), ('b', 'd', 'e', 'a', 'c'),
        ('b', 'd', 'e', 'c', 'a'), ('b', 'e', 'a', 'c', 'd'), ('b', 'e', 'a', 'd', 'c'),
        ('b', 'e', 'c', 'a', 'd'), ('b', 'e', 'c', 'd', 'a'), ('b', 'e', 'd', 'a', 'c'),
        ('b', 'e', 'd', 'c', 'a'), ('c', 'a', 'b', 'd', 'e'), ('c', 'a', 'b', 'e', 'd'),
        ('c', 'a', 'd', 'b', 'e'), ('c', 'a', 'd', 'e', 'b'), ('c', 'a', 'e', 'b', 'd'),
        ('c', 'a', 'e', 'd', 'b'), ('c', 'b', 'a', 'd', 'e'), ('c', 'b', 'a', 'e', 'd'),
        ('c', 'b', 'd', 'a', 'e'), ('c', 'b', 'd', 'e', 'a'), ('c', 'b', 'e', 'a', 'd'),
        ('c', 'b', 'e', 'd', 'a'), ('c', 'd', 'a', 'b', 'e'), ('c', 'd', 'a', 'e', 'b'),
        ('c', 'd', 'b', 'a', 'e'), ('c', 'd', 'b', 'e', 'a'), ('c', 'd', 'e', 'a', 'b'),
        ('c', 'd', 'e', 'b', 'a'), ('c', 'e', 'a', 'b', 'd'), ('c', 'e', 'a', 'd', 'b'),
        ('c', 'e', 'b', 'a', 'd'), ('c', 'e', 'b', 'd', 'a'), ('c', 'e', 'd', 'a', 'b'),
        ('c', 'e', 'd', 'b', 'a'), ('d', 'a', 'b', 'c', 'e'), ('d', 'a', 'b', 'e', 'c'),
        ('d', 'a', 'c', 'b', 'e'), ('d', 'a', 'c', 'e', 'b'), ('d', 'a', 'e', 'b', 'c'),
        ('d', 'a', 'e', 'c', 'b'), ('d', 'b', 'a', 'c', 'e'), ('d', 'b', 'a', 'e', 'c'),
        ('d', 'b', 'c', 'a', 'e'), ('d', 'b', 'c', 'e', 'a'), ('d', 'b', 'e', 'a', 'c'),
        ('d', 'b', 'e', 'c', 'a'), ('d', 'c', 'a', 'b', 'e'), ('d', 'c', 'a', 'e', 'b'),
        ('d', 'c', 'b', 'a', 'e'), ('d', 'c', 'b', 'e', 'a'), ('d', 'c', 'e', 'a', 'b'),
        ('d', 'c', 'e', 'b', 'a'), ('d', 'e', 'a', 'b', 'c'), ('d', 'e', 'a', 'c', 'b'),
        ('d', 'e', 'b', 'a', 'c'), ('d', 'e', 'b', 'c', 'a'), ('d', 'e', 'c', 'a', 'b'),
        ('d', 'e', 'c', 'b', 'a'), ('e', 'a', 'b', 'c', 'd'), ('e', 'a', 'b', 'd', 'c'),
        ('e', 'a', 'c', 'b', 'd'), ('e', 'a', 'c', 'd', 'b'), ('e', 'a', 'd', 'b', 'c'),
        ('e', 'a', 'd', 'c', 'b'), ('e', 'b', 'a', 'c', 'd'), ('e', 'b', 'a', 'd', 'c'),
        ('e', 'b', 'c', 'a', 'd'), ('e', 'b', 'c', 'd', 'a'), ('e', 'b', 'd', 'a', 'c'),
        ('e', 'b', 'd', 'c', 'a'), ('e', 'c', 'a', 'b', 'd'), ('e', 'c', 'a', 'd', 'b'),
        ('e', 'c', 'b', 'a', 'd'), ('e', 'c', 'b', 'd', 'a'), ('e', 'c', 'd', 'a', 'b'),
        ('e', 'c', 'd', 'b', 'a'), ('e', 'd', 'a', 'b', 'c'), ('e', 'd', 'a', 'c', 'b'),
        ('e', 'd', 'b', 'a', 'c'), ('e', 'd', 'b', 'c', 'a'), ('e', 'd', 'c', 'a', 'b'),
        ('e', 'd', 'c', 'b', 'a')]


def product_test():
    """
    Function for testing product from main
    """
    assert list(product('HOPE', repeat=3)) == [('H', 'H', 'H'), ('H', 'H', 'O'), ('H', 'H', 'P'),
        ('H', 'H', 'E'), ('H', 'O', 'H'), ('H', 'O', 'O'), ('H', 'O', 'P'), ('H', 'O', 'E'),
        ('H', 'P', 'H'), ('H', 'P', 'O'), ('H', 'P', 'P'), ('H', 'P', 'E'), ('H', 'E', 'H'),
        ('H', 'E', 'O'), ('H', 'E', 'P'), ('H', 'E', 'E'), ('O', 'H', 'H'), ('O', 'H', 'O'),
        ('O', 'H', 'P'), ('O', 'H', 'E'), ('O', 'O', 'H'), ('O', 'O', 'O'), ('O', 'O', 'P'),
        ('O', 'O', 'E'), ('O', 'P', 'H'), ('O', 'P', 'O'), ('O', 'P', 'P'), ('O', 'P', 'E'),
        ('O', 'E', 'H'), ('O', 'E', 'O'), ('O', 'E', 'P'), ('O', 'E', 'E'), ('P', 'H', 'H'),
        ('P', 'H', 'O'), ('P', 'H', 'P'), ('P', 'H', 'E'), ('P', 'O', 'H'), ('P', 'O', 'O'),
        ('P', 'O', 'P'), ('P', 'O', 'E'), ('P', 'P', 'H'), ('P', 'P', 'O'), ('P', 'P', 'P'),
        ('P', 'P', 'E'), ('P', 'E', 'H'), ('P', 'E', 'O'), ('P', 'E', 'P'), ('P', 'E', 'E'),
        ('E', 'H', 'H'), ('E', 'H', 'O'), ('E', 'H', 'P'), ('E', 'H', 'E'), ('E', 'O', 'H'),
        ('E', 'O', 'O'), ('E', 'O', 'P'), ('E', 'O', 'E'), ('E', 'P', 'H'), ('E', 'P', 'O'),
        ('E', 'P', 'P'), ('E', 'P', 'E'), ('E', 'E', 'H'), ('E', 'E', 'O'), ('E', 'E', 'P'),
        ('E', 'E', 'E')]

    product_object = product('xy', 'ab')
    assert next(product_object) == ('x', 'a')
    assert next(product_object) == ('x', 'b')
    assert next(product_object) == ('y', 'a')
    assert next(product_object) == ('y', 'b')
