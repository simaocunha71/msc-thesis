from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # Create a dictionary to store the count of each number
    counts = {}
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    # Create a new list to store the numbers that occur only once
    result = []
    for number in numbers:
        if counts[number] == 1:
            result.append(number)

    return result

# Test the function
print(remove_duplicates([1, 2, 3, 2, 4]))  # Output: [1, 3, 4]