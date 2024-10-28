from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [
        *numbers[:-1],
        *(delimeter,) * (len(numbers) - 1),
        numbers[-1],
    ]
