def sum_range_list(num_list, start, end):
    return sum(num_list[start:end+1])

def test_sum_range_list():
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29

test_sum_range_list()


"""
def sum_range_list(num_list, start, end):
    return sum(num_list[start:end+1])

def test_sum_range_list():
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29

test_sum_range_list()
"""

# As a side note, the above code is a simple and straightforward solution to the problem. However, it may not be the most efficient one. For instance, if the range is large, it may take significant amount of time to calculate the sum.

# Here's an alternative solution that may be more efficient in terms of time complexity:

def sum_range_list(num_list, start, end):
    return sum(num_list[:end+1]) - sum(num_list[:start])

def test_sum_range_list():
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29

test_sum_range_list()
"""
def sum_range_list(num_list, start, end):
    return sum(num_list[:end+1]) - sum(num_list[:start])

def test_sum_range_list():
    assert sum_range_list([2,1,5,6,8,3,4,9,10,11,8,12], 8, 10) == 29

test_sum_range_list()
"""

# This solution calculates the sum of the entire list and then subtracts the