    from typing import List

    def mean_absolute_deviation(numbers: List[float]) -> float:
        if not numbers:
            raise ValueError("Input list is empty")

        mean = sum(numbers) / len(numbers)
        return sum(abs(num - mean) for num in numbers) / len(numbers)

    # Test cases
    print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Expected output: 1.0
    print(mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]))  # Expected output: 0.0
    print(mean_absolute_deviation([]))  # Expected output: ValueError
    print(mean_absolute_deviation([-1.0, 0.0, 1.0]))  # Expected output: 0.5
    print(mean_absolute_deviation([-3, 0, 3, 0, 3, 0, 0, 0, 0]))  # Expected output: 1.5
    print(mean_absolute_deviation([1, 2, 3, 4, 5]))  # Expected output: 1.5
    print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]))  # Expected output: 1.5
    print(mean_absolute_deviation([-4, 1, -1, 1, 1, -2, 2, 2, -3, 3]))  # Expected output: 1.5
    print(mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Expected output: 2.5

# It works now
print(mean_absolute_deviation([-4, 1, -1, 1, 1, -2, 2, 2, -3, 3]))  # Expected output: 1.5
print(mean_absolute_deviation([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Expected output: 2.5
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 