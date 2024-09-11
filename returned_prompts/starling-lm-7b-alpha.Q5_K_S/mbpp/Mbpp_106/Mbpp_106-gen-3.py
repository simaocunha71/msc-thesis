def add_lists(list1, tuple1):
    return tuple1 + list1

def test_add_lists():
    assert add_lists([5, 6, 7], (9, 10)) == (9, 10, 5, 6, 7)

test_add_lists()

"""
def add_lists(list1, tuple1):
    return tuple(list1 + tuple1)
"""

"""
def add_lists(list1, tuple1):
    return tuple1[:] + list1
"""

"""
def add_lists(list1, tuple1):
    list1.extend(tuple1)
    return tuple1
"""

"""
def add_lists(list1, tuple1):
    for i in tuple1:
        list1.append(i)
    return tuple1
"""

"""
def add_lists(list1, tuple1):
    list1 = list1 + tuple1
    return tuple(list1)
"""


"""
def add_lists(list1, tuple1):
    return tuple(list(tuple1) + list1)
"""


"""
def add_lists(list1, tuple1):
    return tuple(tuple1) + list1
"""

"""
def add_lists(list1, tuple1):
    return tuple(list1) + tuple1
"""

"""
def add_lists(list1, tuple1):
    return tuple(list1) + tuple(tuple1)
"""

"""
def add_lists(list1, tuple1):
    return tuple(list1 + tuple1)
"""

"""
def add_lists(list1, tuple1):
    return tuple(tuple1) + tuple(list1)
"""

"""
def add_lists(list1, tuple1):
    return tuple(tuple1) + list1
"""

"""
def add_lists(list1, tuple1):
    return tuple(tuple1) + tuple(list1)
"""

"""
def add_lists(list1, tuple1):
    return tuple(tuple1) + tuple(list1)
"""

"""
def add_