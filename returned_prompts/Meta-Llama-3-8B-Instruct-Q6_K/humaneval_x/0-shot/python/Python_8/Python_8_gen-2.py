from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1

    total_sum = sum(numbers)
    total_product = 1
    for num in numbers:
        total_product *= num

    return total_sum, total_product

# Example usage:
print(sum_product([]))  # Output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Output: (10, 24)
print(sum_product([5, 5, 5]))  # Output: (15, 125)
print(sum_product([-1, 0, 1]))  # Output: (0, -1)
print(sum_product([-1, 1]))  # Output: (0, -1)  # Product is negative
print(sum_product([-1, -1]))  # Output: (-2, 1)  # Product is positive
print(sum_product([-1, -1, -1]))  # Output: (-3, -1)  # Product is negative
print(sum_product([-1, 0]))  # Output: (-1, 0)
print(sum_product([1]))  # Output: (1, 1)
print(sum_product([5]))  # Output: (5, 5)  # Product is positive
print(sum_product([-1]))  # Output: (-1, -1)  # Product is negative
print(sum_product([1, 1]))  # Output: (2, 1)  # Product is 1
print(sum_product([1, 2]))  # Output: (3, 2)  # Product is 2
print(sum_product([1, 2, 3]))  # Output: (6, 6)  # Product is 6
print(sum_product([1, 2, 3, 4, 5]))  # Output: (15, 120)  # Product is 120
print(sum_product([1, 2, 3, 4, 5, 6]))  # Output: (21, 720)  # Product is 720
print(sum_product([1, 2, 3, 4, 5, 6, 7]))  # Output: (28, 5040)  # Product is 5040
print(sum