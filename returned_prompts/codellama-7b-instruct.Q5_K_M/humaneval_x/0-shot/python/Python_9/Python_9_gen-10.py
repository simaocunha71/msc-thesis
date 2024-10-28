from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    result = []
    for i in range(len(numbers)):
        if i == 0:
            result.append(numbers[i])
        else:
            result.append(max(result[-1], numbers[i]))
    return result
