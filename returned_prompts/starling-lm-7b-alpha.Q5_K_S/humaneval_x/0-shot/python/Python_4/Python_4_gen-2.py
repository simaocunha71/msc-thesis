    from typing import List
    from math import mean

    def mean_absolute_deviation(numbers: List[float]) -> float:
        return mean([abs(x - mean(numbers)) for x in numbers])


# Run tests
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Expect: 1.0
print(mean_absolute_deviation([-1.0, 0.0, 1.0, 2.0, 3.0]))  # Expect: 1.0
print(mean_absolute_deviation([-100.0, 0.0, 100.0]))  # Expect: 100.0


# Test with negative numbers
print(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]))  # Expect: 1.0
print(mean_absolute_deviation([-10.0, -5.0, 0.0, 5.0, 10.0]))  # Expect: 5.0


# Test with more than 5 numbers
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]))  # Expect: 1.5
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]))  # Expect: 2.0


# Test with zeroes
print(mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]))  # Expect: 0.0
print(mean_absolute_deviation([-1.0, 0.0, 1.0, 0.0]))  # Expect: 0.5


# Test with a single number
print(mean_absolute_deviation([1.0]))  # Expect: 0.0
print(mean_absolute_deviation([-1.0]))  # Expect: 0