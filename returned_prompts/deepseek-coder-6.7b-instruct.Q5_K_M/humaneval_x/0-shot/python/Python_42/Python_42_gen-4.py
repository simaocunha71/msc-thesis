

def incr_list(l: list):
    return [x+1 for x in l]


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


def incr_list(l: list):
    return list(map(lambda x: x+1, l))


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


def incr_list(l: list):
    return list(map(add, l, [1]*len(l)))


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


def incr_list(l: list):
    return [x+y for x, y in zip(l, [1]*len(l))]


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


def incr_list(l: list):
    return list(starmap(add, zip(l, [1]*len(l))))


print(incr_list([1, 2, 3]))
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))


from operator import add
from itertools import starmap


def incr_list(l: list):
    return list(starmap(add, zip(l, iter([1]*len(l)))))


print(incr_list([1, 2, 3]))
print(incr_list([5, 