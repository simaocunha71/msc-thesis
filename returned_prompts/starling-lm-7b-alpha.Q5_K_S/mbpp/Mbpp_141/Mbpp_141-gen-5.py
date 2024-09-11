"""
def pancake_sort(a):
    from copy import copy
    while True:
        max_index = a.index(max(a))
        tmp = copy(a)
        tmp.pop(max_index)
        tmp.insert(0, tmp.pop())
        if tmp == sorted(tmp):
            break
        a = copy(tmp)
    return a
"""

def pancake_sort(a):
    tmp = copy(a)
    tmp.sort()
    while True:
        max_index = a.index(max(a))
        tmp.pop(max_index)
        tmp.insert(0, tmp.pop())
        if tmp == a:
            break
        a = copy(tmp)
    return a


"""
def pancake_sort(a):
    from copy import copy
    while True:
        max_index = a.index(max(a))
        tmp = copy(a)
        tmp.pop(max_index)
        tmp.insert(0, tmp.pop(0))
        if tmp == sorted(tmp):
            break
        a = copy(tmp)
    return a
"""


def pancake_sort(a):
    from copy import copy
    while True:
        max_index = a.index(max(a))
        tmp = copy(a)
        tmp.pop(max_index)
        tmp.insert(0, tmp.pop(0))
        if tmp == sorted(tmp):
            break
        a = copy(tmp)
    return a


def pancake_sort(a):
    from copy import copy
    while True:
        max_index = a.index(max(a))
        tmp = copy(a)
        tmp.pop(max_index)
        tmp.insert(0, tmp.pop(0))
        if tmp == sorted(tmp):
            break
        a = copy(tmp)
    return a


def pancake_sort(a):
    from copy import copy
    while True:
        max_index = a.index(max(a))
        tmp = copy(a)
        tmp.