"""
Team project for discrette math
"The analogue of itertools"
"""
from typing import Iterable, Iterator


def count(start: int, step=1) -> Iterator | str:
    """
    Function that replace itertool's count method.
    The given one returns an endless iterator with given start and step, if needed(step is optional)

    :param start: the number, which is a start of the iteration
    :type start: int
    :param step: the step through which the iteration will occur
    :type step: int
    :return: infinite loop iterator
    """
    assert isinstance(start, int), 'Type valid type of parametr(int).'
    default_step = 0
    while True:
        if step:
            yield start + default_step * step
        else:
            yield start + default_step
        default_step += 1


def cycle(iterable: Iterable) -> Iterator:
    """
    Function that replace itertool's cycle method
    Returns an endless iterator by looping through the values of the iterator "iterable"

    :param iterable: the iterated object on which the iteration will take place
    :type iterable: Iterable
    :return: infinite loop iterator
    """
    assert isinstance(iterable, Iterable), 'Type valid type of parametr(iterable).'
    while True:
        for i in iterable:
            yield i


def repeat(value):
    """
    Function that replace itertool's repeat method
    Returns an infinite iterator of repeated value values

    :param value: value which will be iterate
    :type value: any
    :return: infinite loop operator
    """
    while True:
        yield value


def combinations_with_replacement(iterable, lenth):
    """
    Return r length subsequences of elements from the input
    iterable allowing individual elements to be repeated more than once.
    >>> print(list(combinations_with_replacement('ABC', 2)))
    [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
    >>> print(list(combinations_with_replacement('MATH', 3)))
    [('M', 'M', 'M'), ('M', 'M', 'A'), ('M', 'M', 'T'), ('M', 'M', 'H'), ('M', 'A', 'A'),\
 ('M', 'A', 'T'), ('M', 'A', 'H'), ('M', 'T', 'T'), ('M', 'T', 'H'), ('M', 'H', 'H'),\
 ('A', 'A', 'A'), ('A', 'A', 'T'), ('A', 'A', 'H'), ('A', 'T', 'T'), ('A', 'T', 'H'),\
 ('A', 'H', 'H'), ('T', 'T', 'T'), ('T', 'T', 'H'), ('T', 'H', 'H'), ('H', 'H', 'H')]
    >>> print(list(combinations_with_replacement('33231', 2)))
    [('3', '3'), ('3', '3'), ('3', '2'), ('3', '3'), ('3', '1'), ('3', '3'), ('3', '2'),\
 ('3', '3'), ('3', '1'), ('2', '2'), ('2', '3'), ('2', '1'), ('3', '3'), ('3', '1'), ('1', '1')]
    """
    elements = tuple(i for i in iterable)
    lst = product2(range(len(elements)), repeat = lenth)
    for tup in lst:
        sort_tup = tuple(el for el in sorted(tup))
        if sort_tup == tup:
            yield tuple(elements[i] for i in tup)


def permutations(iterable, length=None):
    """
    Function that replaces itertool`s permutations method.
    Returns an iterator of permutations. If length is given,
    returns permutations of a given length.

    :param iterable: an object to permutate
    :type iterable: any
    :param length: length of a permutation
    :type length: int
    :return: infinite loop iterator
    """
    tuple_of_iterables = tuple(iterable)
    tuple_length = len(tuple_of_iterables)
    if length is None:
        tuple_length = length
    if length > tuple_length:
        return None
    indices = [i for i in range(tuple_length)]
    cycles = [i for i in range(tuple_length, tuple_length-length, -1)]
    yield tuple(tuple_of_iterables[i] for i in indices[:length])
    while tuple_length:
        for i in range(length)[::-1]:
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = tuple_length - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(tuple_of_iterables[i] for i in indices[:length])
                break
        else:
            return None
  