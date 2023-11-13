from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

    current_max = None
    maxes: List[int] = []

    for idx in range(len(numbers)):
        if not current_max:
            current_max = numbers[idx]
        elif current_max <= numbers[idx]:
            continue
        else:
            curr_max = current_max
            maxes.append(curr_max)
            current_max = numbers[idx]
    if current_max != None and not (current_max == 0):
        maxes.append(current_max)

    return maxes
