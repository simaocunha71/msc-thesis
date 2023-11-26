from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    def distance(x: float, y: float):
        return (abs(x-y))**2

    for index1 in range(len(numbers)-1, -1, -1):
        if index1 == 0 or has_close_elements_helper([numbers[index1], numbers[index1+1]], threshold)[0]:
            continue
        else:
            break

    return True
