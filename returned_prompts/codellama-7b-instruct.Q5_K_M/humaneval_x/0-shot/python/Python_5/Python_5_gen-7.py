from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return delimeter.join(numbers)
