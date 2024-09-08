
def find_remainder(lst: list, n: int) -> int:
    product = 1
    for num in lst:
        product = (product * num) % n
    return product

print(find_remainder([ 100, 10, 5, 25, 35, 14 ], 11))

# Output: 9

Explanation:

The array elements are multiplied one by one and at each step the result is calculated modulo n. This is done to keep the number small and manageable. Finally, the function returns the result.
"""

assert find_remainder([ 100, 10, 5, 25, 35, 14 ], 11) == 9

# Output: 9

Explanation:

The array elements are multiplied one by one and at each step the result is calculated modulo n. This is done to keep the number small and manageable. Finally, the function returns the result.
"""

assert find_remainder([ 100, 10, 5, 25, 35, 14 ], 11) == 9

# Output: 9

Explanation:

The array elements are multiplied one by one and at each step the result is calculated modulo n. This is done to keep the number small and manageable. Finally, the function returns the result.
"""
<jupyter_output>
9
<jupyter_text>
Task 5
<jupyter_code>
"""
