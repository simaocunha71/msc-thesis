"""
The function max_product is defined to take a list of integers as input and return the maximum product formed by multiplying numbers of an increasing subsequence of that array.

The function works by iterating over the list of numbers and maintaining the maximum product obtained so far and the maximum product ending at the current position.

When iterating over the list of numbers, for each number, we calculate the maximum product ending at the current position as the maximum between the current number and the maximum product ending at the previous position multiplied by the current number.

Finally, we return the maximum product obtained so far, which is the maximum product of any increasing subsequence of the array.
"""
"""

def max_product(numbers):
    max_prod = numbers[0]
    curr_prod = numbers[0]

    for num in numbers[1:]:
        curr_prod = max(num, curr_prod * num)
        max_prod = max(max_prod, curr_prod)

    return max_prod
"""
The function max_product is defined to take a list of integers as input and return the maximum product formed by multiplying numbers of an increasing subsequence of that array.

The function works by iterating over the list of numbers and maintaining the maximum product obtained so far and the maximum product ending at the current position.

When iterating over the list of numbers, for each number, we calculate the maximum product ending at the current position as the maximum between the current number and the maximum product ending at the previous position multiplied by the current number.

Finally, we return the maximum product obtained so far, which is the maximum product of any increasing subsequence of the array.
"""
"""

def max_product(numbers):
    max_prod = numbers[0]
    curr_prod = numbers[0]

    for num in numbers[1:]:
        curr_prod = max(num, curr_prod * num)
        max_prod = max(max_prod, curr_prod)

    return max_prod

assert max_product([3, 100, 4, 5, 150, 6]) == 3000
"""
This function will return the maximum product formed by multiplying numbers of an increasing