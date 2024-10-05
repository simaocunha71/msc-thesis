def sum_product(numbers: List[int]) -> Tuple[int, int]:
    total_sum = 0
    total_product = 1
    for num in numbers:
        total_sum += num
        total_product *= num
    return (total_sum, total_product)

# Test Cases
assert sum_product([]) == (0, 1)
assert sum_product([1, 2, 3, 4]) == (10, 24)

print("All test cases pass")

Here, we define a function called sum_product which takes a list of integers and returns a tuple. The tuple contains the sum of all the integers in the list and the product of all the integers in the list. If the list is empty, the sum is 0 and the product is 1. We use a for loop to iterate over the list, adding each number to the total_sum and multiplying the total_product by the number. Finally, we return the total_sum and total_product as a tuple.

This solution has a time complexity of O(n), where n is the length of the input list. This is because we are iterating over the list once. The space complexity is also O(n), as we are storing the sum and product in separate variables.

Note: This solution assumes that the input is always a list of integers. If this is not the case, you should add error checking to handle non-integer inputs.
"""

# Test Cases
assert sum_product([]) == (0, 1)
assert sum_product([1, 2, 3, 4]) == (10, 24)

print("All test cases pass")
<jupyter_output>
All test cases pass
<jupyter_text>
Question 2:
<jupyter_code>
"""
