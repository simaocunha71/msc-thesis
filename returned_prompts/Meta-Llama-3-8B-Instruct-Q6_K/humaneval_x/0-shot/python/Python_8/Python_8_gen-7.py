from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1

    total_sum = 0
    total_product = 1

    for num in numbers:
        total_sum += num
        total_product *= num

    return total_sum, total_product
    



# Testing the function
print(sum_product([]))  # Expected output: (0, 1)
print(sum_product([1, 2, 3, 4]))  # Expected output: (10, 24)
print(sum_product([-1, -2, -3, -4]))  # Expected output: (-10, -24)
print(sum_product([1, 1, 1, 1]))  # Expected output: (4, 1)
print(sum_product([2, 3, 4, 5]))  # Expected output: (14, 60)
print(sum_product([0, 0, 0, 0]))  # Expected output: (0, 0)
print(sum_product([10, 20, 30, 40]))  # Expected output: (100, 24000)
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Expected output: (55, 3628800) 
print(sum_product([-1, 2, 3, 4, 5]))  # Expected output: (13, -60)
print(sum_product([10, 20, 30, 40, 50]))  # Expected output: (150, 6000000)
print(sum_product([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  # Expected output: (10, 1)
print(sum_product([-10, -9, -8, -7, -6]))  # Expected output: (-40, -362880) 
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))  # Expected output: (78, 3628800)
print(sum_product([-1, -2, -3, -4,