from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    smallest_difference = float("inf")
    first_closest = None
    second_closest = None

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            difference = abs(numbers[j] - numbers[i])
            if difference < smallest_difference:
                smallest_difference = difference
                first_closest = numbers[i]
                second_closest = numbers[j]

    return (first_closest, second_closest)
