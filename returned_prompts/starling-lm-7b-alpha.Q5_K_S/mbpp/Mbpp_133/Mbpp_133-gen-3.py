def sum_negativenum(nums):
    return sum([num for num in nums if num < 0])

# Unit Test
print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])) # -32



















"""
def sum_negativenum(nums):
    sum = 0
    for num in nums:
        if num < 0:
            sum += num
    return sum
"""


"""
def sum_negativenum(nums):
    return sum(filter(lambda num: num < 0, nums))
"""


"""
def sum_negativenum(nums):
    return sum([num for num in nums if num < 0])
"""


"""
def sum_negativenum(nums):
    return sum(nums) if sum(nums) < 0 else 0
"""


"""
def sum_negativenum(nums):
    return reduce(lambda a, b: a + b, filter(lambda num: num < 0, nums))
"""

```