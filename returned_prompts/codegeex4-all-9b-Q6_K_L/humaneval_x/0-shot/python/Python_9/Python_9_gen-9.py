from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    # Create an empty list to store the rolling maximum
    rolling_max_list = []

    # Iterate through the list of numbers
    for i, num in enumerate(numbers):
        # If the list is empty or the current number is greater than the last element in the rolling max list,
        # append the current number to the list
        if not rolling_max_list or num > rolling_max_list[-1]:
            rolling_max_list.append(num)
        # Otherwise, append the last element in the rolling max list to the list
        else:
            rolling_max_list.append(rolling_max_list[-1])

    return rolling_max_list

# Test the function
print(rolling_max([1, 2, 3, 2, 3, 4, 2])) # [1, 2, 3, 3, 3, 4, 4]
print(rolling_max([1, 2, 3, 2, 3, 4, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [1, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 9, 10, 10]
print(rolling_max([-1, -2, -3, -2, -3, -4, -2])) # [-1, -1, -1, -1, -1, -1, -1]
print(rolling_max([-1, -2, -3, -2, -3, -4, -2, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10])) # [-1, -1, -1, -1, -1, -1, -1, -1, -1,