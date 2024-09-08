
def two_unique_nums(nums):
    return list(set(nums))

print(two_unique_nums([1,2,3,2,3,4,5]))

"""

Explanation:

The function `two_unique_nums(nums)` takes a list of numbers as an argument.

We use the `set()` function to remove duplicate numbers from the list. 

The `set()` function returns a set of unique elements from the list. 

But a set in python is an unordered collection of items. So the order of elements in the resultant list may not be the same as in the input list.

So, we convert the set back to a list using the `list()` function.

Finally, we return the list.
"""
<jupyter_output>
[1, 2, 3, 4, 5]
<jupyter_text>
Question 2
<jupyter_code>
"""
