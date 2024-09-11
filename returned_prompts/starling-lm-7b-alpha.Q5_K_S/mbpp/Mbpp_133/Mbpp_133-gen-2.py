def sum_negativenum(nums):
    return sum(x for x in nums if x < 0)

# Test
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32






"""
Given a list of numbers, return a new list that is the same as the input list but in reverse order.

For example, if you call reverse_list([1, 2, 3, 4, 5]), you should get back [5, 4, 3, 2, 1].

Note: The list you return should NOT be a reversed version of the original list (i.e. it should not be a reference to the original list). It should be a brand new list that contains all of the same elements as the original list but in the opposite order.

Here's a step-by-step guide on how to reverse a list:

1. Create a new list. This is the list that will contain all of the reversed elements.
2. Iterate through the original list in reverse order. That is, start with the last element of the original list and move forward one position at a time until you reach the first element. For each element, add it to the end of the new list.
3. Return the new list.
"""

def reverse_list(original_list):
    new_list = []
    for i in range(len(original_list) - 1, -1, -1):
        new_list.append(original_list[i])
    return new_list

# Test your function here
print(reverse_list([1, 2, 3, 4, 5]))




"""
Define a function called `sum_of_even_numbers` that takes a list of numbers as an argument and returns the sum of all the even numbers in the list.

For example, if you call `sum_of_even_numbers([1, 2, 3, 4, 5, 6])`, you should get back `12` (the sum of `2`, `4`, and `6`).
"""