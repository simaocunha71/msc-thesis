from itertools import *
def max_sum_list(lst):
    return max(lst, key=sum)

def test_max_sum_list():
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]

test_max_sum_list()



"""
def max_sum_list(lst):
    return max(lst, key = lambda x:sum(x))
"""


def max_sum_list(lst):
    sum_list = [sum(i) for i in lst]
    max_list = max(sum_list)
    return [i for i in lst if sum(i)==max_list]

def test_max_sum_list():
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]

test_max_sum_list()

"""
def max_sum_list(lst):
    max_list = [max(i) for i in lst]
    return [i for i in lst if max(i) == max(max_list)]
"""

def max_sum_list(lst):
    return max(lst, key = sum)

def test_max_sum_list():
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]

test_max_sum_list()

"""
def max_sum_list(lst):
    return max(lst, key = lambda x:sum(x))
"""

def max_sum_list(lst):
    sum_list = [sum(i) for i in lst]
    max_list = max(sum_list)
    return [i for i in lst if sum(i)==max_list]

def