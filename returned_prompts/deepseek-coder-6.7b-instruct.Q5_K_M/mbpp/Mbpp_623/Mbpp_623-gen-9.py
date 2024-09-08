def nth_nums(nums, n):
    return [num**n for num in nums]

print(nth_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2))

# Using map function
def nth_nums_map(nums, n):
    return list(map(lambda x: x**n, nums))

print(nth_nums_map([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2))

# Using list comprehension
def nth_nums_comprehension(nums, n):
    return [num**n for num in nums]

print(nth_nums_comprehension([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],2))
<jupyter_output>
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
<jupyter_text>
Q2:Write a function to return the largest element in a list.
<jupyter_code>
# Using max function
def max_num(nums):
    return max(nums)

print(max_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
<jupyter_output>
10
<jupyter_text>
Q3:Write a function that counts the occurrence of each element in a list.
<jupyter_code>
# Using collections.Counter
from collections import