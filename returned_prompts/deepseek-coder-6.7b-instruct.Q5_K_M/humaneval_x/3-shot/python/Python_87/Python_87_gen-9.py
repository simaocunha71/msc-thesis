    coordinates = []
    for i, row in enumerate(lst):
        for j, element in enumerate(row):
            if element == x:
                coordinates.append((i, j))

    return sorted(coordinates, key=lambda x: (x[0], -x[1]))

I'm not sure if you are looking for a solution in Python or JavaScript, but I've provided solutions in both languages. If you meant different things, please specify.

A: Here is the Python solution:
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < threshold:
            return True
    return False


