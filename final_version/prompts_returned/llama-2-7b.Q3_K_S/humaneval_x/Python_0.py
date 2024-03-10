from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    if not numbers:
        return False
    first = float('inf')  # inf is used to avoid division by 0
    for num in sorted(numbers):
        dist = abs(num - first)
        if dist < threshold and dist > 0.01:
            return True
        first = num
    return False