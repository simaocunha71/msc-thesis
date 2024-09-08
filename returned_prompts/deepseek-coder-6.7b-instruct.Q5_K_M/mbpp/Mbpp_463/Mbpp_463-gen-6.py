The given array is: [1, -2, -3, 0, 7, -8, -2]

The maximum product subarray is [7, -8, -2]. The product of this subarray is 112.

def max_subarray_product(lst):
    max_end_here = max_end_so_far = 1
    for i in lst:
        if i == 0:
            max_end_here = max_end_so_far = 1
        else:
            max_end_here = max(i, max_end_here * i)
            max_end_so_far = max(max_end_so_far, max_end_here)
    return max_end_so_far

print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))

"""
Explanation:

The function works by using two variables max_end_here and max_end_so_far. The variable max_end_here stores the maximum product ending at the current position and the variable max_end_so_far stores the maximum product encountered so far.

The function iterates over each number in the given list. For each number, it updates max_end_here as the maximum between the current number and the product of max_end_here and the current number. It then updates max_end_so_far as the maximum between max_end_so_far and max_end_here.

If the current number is 0, it resets max_end_here and max_end_so_far to 1.

Finally, the function returns the value stored in max_end_so_far which is the maximum product subarray in the given list.
"""
<jupyter_output>
112
<jupyter_text>
Q2:
<jupyter_code>
"""
