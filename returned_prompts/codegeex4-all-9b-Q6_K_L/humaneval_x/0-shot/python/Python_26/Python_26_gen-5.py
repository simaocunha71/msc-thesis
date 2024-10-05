from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create a dictionary to store the count of each number
    counts = {}
    # Loop through the list of numbers
    for num in numbers:
        # If the number is already in the dictionary, increment its count
        if num in counts:
            counts[num] += 1
        # Otherwise, add the number to the dictionary with a count of 1
        else:
            counts[num] = 1
    
    # Create a new list to store the numbers that occur only once
    result = []
    # Loop through the list of numbers again
    for num in numbers:
        # If the count of the number is 1, add it to the result list
        if counts[num] == 1:
            result.append(num)
    
    # Return the result list
    return result