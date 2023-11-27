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
    min_nums = [(i, j) for i, j in list(zip(numbers[:-1] + [float('inf')]) if float('inf') != float(j)]
                  for (i, j) in min_nums]
    max_nums = [(f - inf) for f in numbers[1:] if not float('inf') == float(f)]

    nums_diffs = []
    for min, max in zip(min_nums[:-1], max_nums):
        diff = abs(max - min)
        if len(nums_diffs) > 0 and diff < (nums_diffs[-1] + 2 * threshold):
            return True
        nums_diffs.append(diff)
    return False