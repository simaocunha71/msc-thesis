from itertools import product


def max_sum_list(input_list):
    max_sum = 0
    max_sum_list = []
    for item in product(*input_list):
        if sum(item) > max_sum:
            max_sum = sum(item)
            max_sum_list = item
    return max_sum_list


def test_max_sum_list():
    assert max_sum_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == [10, 11, 12]


test_max_sum_list()


"""
The function first uses itertools.product to generate all the possible combinations of the list of lists, and then compares the sum of each combination to determine which one has the highest sum. Finally, the function returns the list with the highest sum.
"""

# 


def max_sum_list(input_list):
    max_sum = 0
    max_sum_list = []
    for item in product(*input_list):
        if sum(item) > max_sum:
            max_sum = sum(item)
            max_sum_list = item
    return max_sum_list


def test_max_sum_list():
    assert max_sum_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]) == [10, 11, 12]


test_max_sum_list()


"""
This implementation uses itertools.product to generate all possible combinations of the list of lists. Then, it compares the sum of each combination to determine which one has the highest sum. Finally, the function returns the list with the highest sum.
"""

# 


def max_sum_list(input_list):
    max_sum = 0
    max_sum_list = []
    for item in product(*input_list):
        if sum(item) > max_sum:
           