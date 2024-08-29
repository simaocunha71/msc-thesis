def kth_element(arr, k):
    arr.sort()
    return arr[k - 1]

print(kth_element([12,3,5,7,19], 2))

"""
Explanation:
This function sorts the array in ascending order and then returns the kth element.
However, remember that the array is 0-indexed, meaning the first element is at index 0.
So, to get the kth element with 1-based indexing, we subtract 1 from k.
"""
<jupyter_output>
3
<jupyter_text>
Question 2
<jupyter_code>
