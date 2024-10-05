from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    return sum(abs(n - mean) for n in numbers) / len(numbers)


print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))

