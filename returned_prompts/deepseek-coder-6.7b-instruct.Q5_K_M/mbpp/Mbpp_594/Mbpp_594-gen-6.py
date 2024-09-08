
def diff_even_odd(nums):
    even_num = next((num for num in nums if num % 2 == 0), None)
    odd_num = next((num for num in nums if num % 2 != 0), None)
    return even_num - odd_num if even_num and odd_num else None

print(diff_even_odd([1,3,5,7,4,1,6,8]))

"""
This function first finds the first even and odd number in the given list using Python's `next` function combined with a generator expression.
It then returns the difference of these two numbers if both were found, otherwise it returns `None`.
"""
<jupyter_output>
3
<jupyter_text>
