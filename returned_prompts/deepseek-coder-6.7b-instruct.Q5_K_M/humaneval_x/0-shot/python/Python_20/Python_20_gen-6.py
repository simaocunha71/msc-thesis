from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()
    min_diff = float('inf')
    result = (None, None)
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i-1], numbers[i])
    return result


print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]))
print(find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]))


This will sort the numbers, then iterate over the sorted list and find the two numbers with the smallest difference. It then returns these two numbers in order as requested.
'''

# Solution 2

'''
