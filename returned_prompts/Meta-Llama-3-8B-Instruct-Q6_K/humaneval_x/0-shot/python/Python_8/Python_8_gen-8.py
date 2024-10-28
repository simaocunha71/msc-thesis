from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return 0, 1
    else:
        sum_val = 0
        product_val = 1
        for num in numbers:
            sum_val += num
            product_val *= num
        return sum_val, product_val
# test cases
print(sum_product([]))  # (0, 1)
print(sum_product([1, 2, 3, 4]))  # (10, 24)
print(sum_product([-1, 0, 1]))  # (0, -1)
print(sum_product([1]))  # (1, 1)
print(sum_product([2, 3, 4]))  # (9, 24) 
print(sum_product([5, 5]))  # (10, 25) 
print(sum_product([10, 20, 30]))  # (60, 6000) 
print(sum_product([-5, 0, 5]))  # (0, 25) 
print(sum_product([-5, -5, -5]))  # (-15, 125) 
print(sum_product([1, 2, 3, 4, 5]))  # (15, 120) 
print(sum_product([1, 2, 3, 4, 5, 6]))  # (21, 720) 
print(sum_product([1, 2, 3, 4, 5, 6, 7]))  # (28, 5040) 
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8]))  # (36, 40320) 
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # (45, 362880) 
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # (55, 3628800) 
print(sum_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))  # (66, 39916800)