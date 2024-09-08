
def sum_Of_Subarray_Prod(arr):
    n = len(arr)
    prod = [0]*n
    sum_val = 0
    for i in range(n):
        if i == 0:
            prod[i] = arr[i]
        else:
            prod[i] = prod[i-1]*arr[i]
    for i in range(n):
        if i == 0:
            sum_val += prod[n-1]*arr[i]
        else:
            sum_val += prod[n-1]//prod[i-1]*arr[i]
    return sum_val

assert sum_Of_Subarray_Prod([1,2,3]) == 20

Explanation:
The sublists of [1,2,3] are [], [1], [2], [3], [1,2], [2,3] and [1,2,3]. The sum of products of these sublists are 1*2*3 + 1*3 + 2*3 + 1*2 + 2*3 + 1*3 + 1*2*3 = 20.
The product of an empty sublist is considered to be 1.
"""

# Test case
print(sum_Of_Subarray_Prod([1,2,3]))
<jupyter_output>
20
<jupyter_text>
Question 2:
<jupyter_code>
"""
