"""
def max_subarray_product(arr):
    max_end_here = max_end_so_far = 1
    max_neg = float('-inf')
    flag = False
    for i in arr:
        if i < 0:
            max_end_here, max_end_so_far = max_end_so_far*i, min(max_end_here*i, 1)
            if max_neg < i:
                max_neg = i
        elif i > 0:
            max_end_here = max_end_here * i
            max_end_so_far = max(max_end_so_far, max_end_here)
        else:
            max_end_here = max_end_so_far = 1
    if max_neg != float('-inf'):
        max_end_so_far = max(max_end_so_far, max_end_here // max_neg)
    return max_end_so_far

print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))
"""

# Correct Answer:
"""
def max_subarray_product(arr):
    if not arr:
        return 0

    max_end_here = max_end_so_far = arr[0]

    for i in arr[1:]:
        if i < 0:
            max_end_here, max_end_so_far = max_end_so_far*i, min(max_end_here*i, 1)
        else:
            max_end_here = max_end_here * i
            max_end_so_far = max(max_end_so_far, max_end_here)

    return max_end_so_far

print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))
"""
<jupyter_output>
112
<jupyter_text>
