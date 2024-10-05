    def rolling_max(numbers: List[int]) -> List[int]:
        return [max(numbers[:i + 1]) for i in range(len(numbers))]


# Another implementation using deque
from collections import deque

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_num = deque([])
    res = []
    for num in numbers:
        while max_num and max_num[-1] < num:
            max_num.pop()
        max_num.append(num)
        res.append(max_num[0])
    return res


# Another implementation using sliding window
def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    return [max(numbers[i:j + 1]) for i, j in zip(range(0, len(numbers)), range(1, len(numbers) + 1))]


# Another implementation using deque and sliding window
from collections import deque

def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    max_num = deque([])