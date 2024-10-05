from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    min_diff = float('inf')
    closest_pair = None
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            diff = abs(numbers[i] - numbers[j])
            if diff < min_diff:
                min_diff = diff
                closest_pair = (numbers[i], numbers[j])
    return closest_pair


def test_find_closest_elements():
    # Test 1:
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)

    # Test 2:
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)


if __name__ == '__main__':
    test_find_closest_elements()
