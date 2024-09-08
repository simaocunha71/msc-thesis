def split_Arr(arr,n):
    arr[:] = arr[n:] + arr[:n]
    return arr

print(split_Arr([12,10,5,6,52,36],2))

"""
Explanation:
In the given problem, we are asked to split a list at the nth element and then add the first part to the end.
The given array is [12,10,5,6,52,36] and we need to split at the 2nd element.
After splitting the array at the 2nd element we get [5,6,52,36] and [12,10].
So, we add the first part [5,6,52,36] to the end of the second part [12,10] to get [5,6,52,36,12,10].
"""
<jupyter_output>
[5, 6, 52, 36, 12, 10]
<jupyter_text>
**Question 2**
<jupyter_code>
