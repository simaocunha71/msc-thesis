from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    min_val, max_val = min(numbers), max(numbers)
    return [
        (number - min_val) / (max_val - min_val)
        for number in numbers
    ]
