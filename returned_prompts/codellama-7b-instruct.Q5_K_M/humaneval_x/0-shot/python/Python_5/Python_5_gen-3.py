from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [numbers[i] if i % 2 == 0 else delimeter for i in range(len(numbers))]
