from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    smallest_diff = float('inf')
    smallest_diff_index_1 = 0
    smallest_diff_index_2 = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            diff = abs(numbers[j] - numbers[i])
            if diff < smallest_diff:
                smallest_diff = diff
                smallest_diff_index_1 = i
                smallest_diff_index_2 = j
    return (numbers[smallest_diff_index_1], numbers[smallest_diff_index_2])
