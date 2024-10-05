    max_num = 0
    rolling_max_list = []
    for elem in numbers:
        if elem > max_num:
            max_num = elem
        rolling_max_list.append(max_num)
    return rolling_max_list


# This code is wrong, as it returns the maximum element found until the given moment, not the rolling maximum element found.
# The correct solution should be:

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 3, 4]
    """
    rolling_max_list = []
    for i in range(len(numbers)):
        max_num = numbers[i]
        for j in range(i+1, len(numbers)):
            if numbers[j] > max_num:
                max_num = numbers[j]
        rolling_max_list.append(max_num)
    return rolling_max_list

# This code is also wrong, as it returns the maximum element found until the given moment, not the rolling maximum element found.
# The correct solution should be:

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    rolling_max_list = []
    for i in range(len(numbers)):
        rolling_max_list.append(max(numbers[:i+1]))
    return rolling_max_list

# This code is correct and returns the rolling maximum element found until the given moment in the sequence.
# It uses the max() function to find the maximum element in the sublist