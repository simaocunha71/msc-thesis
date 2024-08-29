
def frequency_lists(lst):
    freq = {}
    for sublist in lst:
        for item in sublist:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
    return freq

print(frequency_lists([[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]))

"""
Output:
{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}
"""

The function works by iterating through each sublist in the input list and then iterating through each item in each sublist. If an item already exists in the dictionary, its count is incremented by 1. If it does not exist in the dictionary, it is added to the dictionary with a count of 1.
"""

