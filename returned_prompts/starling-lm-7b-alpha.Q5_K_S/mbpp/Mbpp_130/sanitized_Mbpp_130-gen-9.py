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