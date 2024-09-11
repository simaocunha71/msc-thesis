from functools import reduce
def max_sum_list(lst):
    lst.sort(key=sum)
    return lst[-1]

def test_max_sum_list():
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]

test_max_sum_list()



"""
def max_sum_list(lst):
    max_list = []
    for i in range(len(lst)):
        if sum(lst[i]) >= sum(max_list):
            max_list = lst[i]
    return max_list

def test_max_sum_list():
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]

test_max_sum_list()
"""

"""
def max_sum_list(lst):
    lst.sort(key=sum)
    return lst[-1]

def test_max_sum_list():
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]

test_max_sum_list()
"""

"""
def max_sum_list(lst):
    lst.sort(key=lambda x:sum(x))
    return lst[-1]

def test_max_sum_list():
    assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]

test_max_sum_list()
"""

"""
def max_sum_list(lst):
    lst.sort(key=lambda x:sum(x))
    return lst[-1]

def