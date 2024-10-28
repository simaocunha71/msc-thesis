from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total_sum = 0
    total_product = 1
    for num in numbers:
        total_sum += num
        total_product *= num
    return (total_sum, total_product)

print(sum_product([]))
print(sum_product([1, 2, 3, 4]))

Output:
(0, 1)
(10, 24)

Explanation:
The function sum_product() takes a list of integers as input. It initializes two variables, total_sum and total_product, to 0 and 1 respectively. Then, for each number in the input list, it adds the number to total_sum and multiplies the number with total_product. Finally, it returns a tuple with total_sum and total_product. If the list is empty, it returns (0, 1) as expected.
"""

# Exercise 4

"""
