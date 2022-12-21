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
    if len(iterable) < 1:
        return
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


def product(*args, **kwds):
    '''
    :param int args: Set or sets, which should be turned into cartesian product
    :param dict kwds: Number od repetotions
    :returns:  cartesian product of sets
    :rtype: list(tuple)
    '''
    def recursive(arg_list: list):
        '''
        :param list arg_list: List of sets to turn into cartesian product
        :returns: generated object
        :rtype:generator
        '''
        if not arg_list:
            yield()
        else:
            for elem in arg_list[0]:
                for prod in  recursive(arg_list[1:]):
                    yield (elem,)+prod
    try:
        pools = list(map(list, args)) * kwds['repeat']
    except KeyError:
        pools = list(map(list, args))
    for i in  list(recursive(pools)):
        yield i



def combinations(iterable: str | list | tuple, length: int):
    """
    Returns a generator of combinations from n to r elements in a sorted order
    :param iterable: an object to combinate
    :type iterable: iterable
    :param length: length of a combination
    :type length: int
    :return: infinite loop iterator
    """
    if not isinstance(iterable, str) and not isinstance(iterable, list) \
        and not isinstance(iterable, tuple):
        return
    if not isinstance(length, int):
        return
    iterable_length = len(iterable)
    if length > iterable_length:
        return
    indices = list(i for i in range(length))
    rev_indices = indices[::-1]
    yield tuple(iterable[i] for i in indices)

    while True:
        flag = False
        for i in rev_indices:
            if indices[i] != iterable_length - length + i:
                flag = True
                break
        if not flag:
            return
        indices[i] += 1
        for j in range(i+1, length):
            indices[j] = indices[j - 1] + 1
        yield tuple(iterable[i] for i in indices)


def combinations_with_replacement(iterable:Iterable, length:int):
    """
    Return r length subsequences of elements from the input
    iterable allowing individual elements to be repeated more than once.
    """
    assert isinstance(iterable, Iterable), 'Type valid type of parametr(iterable).'
    assert isinstance(length, int), 'Type valid type of parametr(int).'
    elements = tuple(i for i in iterable)
    lst = product(range(len(elements)), repeat=length)
    for tuple_ in lst:
        sort_tup = tuple(el for el in sorted(tuple_))
        if sort_tup == tuple_:
            yield tuple(elements[i] for i in tuple_)


def permutations(iterable:Iterable, length=None):
    """
    Function that replaces itertool`s permutations method.
    Returns an iterator of permutations. If length is given,
    returns permutations of a given length.
    :param iterable: an object to permutate
    :type iterable: iterable
    :param length: length of a permutation
    :type length: int
    :return: infinite loop iterator
    """
    assert isinstance(iterable, Iterable), 'Type valid type of parametr(iterable).'

    tuple_of_iterables = tuple(iterable)
    tuple_length = len(tuple_of_iterables)
    if length is None:
        length = tuple_length
    if not length is None:
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
