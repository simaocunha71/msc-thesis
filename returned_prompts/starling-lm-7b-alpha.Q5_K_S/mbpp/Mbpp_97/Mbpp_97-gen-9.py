def frequency_lists(lst):
    freq = {}
    for el in lst:
        if el in freq:
            freq[el] += 1
        else:
            freq[el] = 1
    return freq




def test_frequency_lists():
    assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

test_frequency_lists()

"""
Write a function to find frequency of each element in a flattened list of lists, returned in a dictionary.

Examples:

frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

"""

"""
Correct Solution:
def frequency_lists(lst):
    freq = {}
    for el in lst:
        if el in freq:
            freq[el] += 1
        else:
            freq[el] = 1
    return freq




def test_frequency_lists():
    assert frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]) == {1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}

test_frequency_lists()

"""

"""
Correct Solution:
def frequency_lists(lst):