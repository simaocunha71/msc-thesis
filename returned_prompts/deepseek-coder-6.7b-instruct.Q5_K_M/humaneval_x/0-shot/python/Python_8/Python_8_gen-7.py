from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if len(numbers) == 0:
        return (0, 1)
    else:
        return (sum(numbers), 1 if len(numbers) == 0 else functools.reduce(lambda x, y: x * y, numbers))

print(sum_product([]))
print(sum_product([1, 2, 3, 4]))

This code uses the reduce function from the functools module to calculate the product of all the numbers in the list. If the list is empty, it returns (0, 1). Otherwise, it returns a tuple containing the sum and product of the numbers in the list.
"""

