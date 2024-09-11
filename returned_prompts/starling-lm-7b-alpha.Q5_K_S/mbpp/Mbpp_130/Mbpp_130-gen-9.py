def max_occurrences(lst):
    """
    Finds the item with maximum frequency in a given list.
    """
    # Initialize a dictionary to keep track of the frequency of each element
    freq_dict = {}
    for elem in lst:
        if elem in freq_dict:
            freq_dict[elem] += 1
        else:
            freq_dict[elem] = 1

    # Initialize a maximum frequency
    max_freq = max(freq_dict.values())

    # Initialize a set to keep track of the elements with maximum frequency
    max_freq_set = {key for key in freq_dict if freq_dict[key] == max_freq}

    return max_freq_set

# Testing the function
assert max_occurrences([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]) == {2}

# Testing with a different list
assert max_occurrences([2, 3, 5, 6, 8, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 5, 2]) == {5}

# Testing with a list with only one element
assert max_occurrences([2]) == {2}

# Testing with an empty list
assert max_occurrences([]) == set()

# Testing with a list with all unique elements
assert max_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9]) == {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Testing with a list with all the same element
assert max_occurrences([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]) == {2}

# Testing