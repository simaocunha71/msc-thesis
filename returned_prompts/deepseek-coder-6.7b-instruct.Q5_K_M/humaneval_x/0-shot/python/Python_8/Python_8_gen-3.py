from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    sum_nums = 0
    product_nums = 1
    for num in numbers:
        sum_nums += num
        product_nums *= num
    return (sum_nums, product_nums)


print(sum_product([]))
print(sum_product([1, 2, 3, 4]))

# Expected Output:
# (0, 1)
# (10, 24)

This function uses a loop to iterate over the list of numbers, adding each number to the sum and multiplying each number with the product. It then returns a tuple containing the sum and product. For an empty list, the sum is 0 and the product is 1 by default, as per the problem statement.
<jupyter_output>
<empty_output>
<jupyter_text>
