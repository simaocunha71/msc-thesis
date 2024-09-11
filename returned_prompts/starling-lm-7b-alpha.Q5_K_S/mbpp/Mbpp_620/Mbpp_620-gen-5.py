```
from fractions import gcd
from functools import reduce

def largest_subset(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    g = reduce(gcd, nums)
    return len([x for x in nums if x % g == 0])
```

Explanation:
Given a list of numbers, we need to find the size of the largest subset of the list so that every pair of numbers is divisible. To solve this problem, we can follow these steps:

1. Find the greatest common divisor (gcd) of all the numbers in the list. This can be done using the `reduce` function from the `functools` module and the `gcd` function from the `fractions` module.
2. Iterate through the list of numbers and count the number of elements that are divisible by the gcd. This can be done using a list comprehension and the modulo operator (%).
3. Return the count of elements that are divisible by the gcd.

The time complexity of this solution is O(n), where n is the length of the input list, since we only need to iterate through the list once.

The space complexity of this solution is O(1), since we are not using any additional data structures that scale with the size of the input list.

Overall, this solution provides an efficient and concise way to find the size of the largest subset of a list of numbers so that every pair is divisible.

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

"""

