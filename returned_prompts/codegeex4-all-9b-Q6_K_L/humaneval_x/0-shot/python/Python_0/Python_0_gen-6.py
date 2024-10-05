from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # Sort the list of numbers
    numbers.sort()

    # Iterate through the sorted list and check if any two numbers are closer than the threshold
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] < threshold:
            return True

    return False

print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))