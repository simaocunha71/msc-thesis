from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    for i in range(len(numbers)):
        current_max = max(numbers[:i + 1])
        result.append(current_max)
    return result


def rolling_max_optimized(numbers: List[int]) -> List[int]:
    return [max(numbers[:i + 1]) for i in range(len(numbers))]
