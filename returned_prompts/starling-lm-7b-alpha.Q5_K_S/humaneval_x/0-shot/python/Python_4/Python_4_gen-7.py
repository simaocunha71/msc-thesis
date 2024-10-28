    from math import fabs
    from typing import List

    mean = sum(numbers) / len(numbers)
    return sum(fabs(x - mean) for x in numbers) / len(numbers)


# Run tests
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Expect: 1.0
print(mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]))  # Expect: 0.0
print(mean_absolute_deviation([5.0, 4.0, 3.0, 2.0]))  # Expect: 1.25
print(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]))  # Expect: 1.0


# Test edge cases
print(mean_absolute_deviation([]))  # Expect: 0.0
print(mean_absolute_deviation([0]))  # Expect: 0.0
print(mean_absolute_deviation([-1]))  # Expect: 1.0
print(mean_absolute_deviation([1]))  # Expect: 0.0
print(mean_absolute_deviation([-1, 1]))  # Expect: 1.0


# Test with large numbers
print(mean_absolute_deviation([10000000.0, 20000000.0, 30000000.0, 40000000.0]))  # Expect: 10000000.0


# Test with negative numbers
print(mean_absolute_deviation([-10.0, -20.0, -30.0, -40.0]))  # Expect: 10.0






























































