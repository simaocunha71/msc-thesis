
def even_position(nums):
    return all(num % 2 == 0 for num in nums[::2])

print(even_position([3,2,1])) # False

"""
Explanation:

The function `even_position` takes a list `nums` as input. 
The expression `nums[::2]` generates a new list with every even-indexed element in `nums`. 
The expression `num % 2 == 0 for num in nums[::2]` generates a generator that yields `True` if the element at the even index is an even number and `False` otherwise. 
The function `all` returns `True` if all elements in the generator are `True` and `False` otherwise. 

So, if every even-indexed number in the list is even, the function returns `True`; otherwise, it returns `False`.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
