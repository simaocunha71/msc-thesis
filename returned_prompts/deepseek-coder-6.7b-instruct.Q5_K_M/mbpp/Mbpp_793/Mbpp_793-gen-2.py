def last(arr, target):
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            return i
    return -1

print(last([1,2,3],1)) # 0
"""
This function works by iterating over the array in reverse order. It returns the index of the first occurrence of the target element it finds. If the element is not found, it returns -1.
"""

# This code is contributed by Bharath Srivastav
<jupyter_output>
0
<jupyter_text>
**Question 3**Given an array of integers, write a function to check whether the array is monotonic (i.e. it is either monotone increasing or monotone decreasing).
<jupyter_code>
