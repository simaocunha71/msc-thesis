
def kth_element(arr, k):
    arr.sort()
    return arr[k-1]

print(kth_element([12,3,5,7,19], 2))

"""
The above function takes in a list and an integer as input and returns the kth smallest element in the list. The function first sorts the list in ascending order and then returns the kth element in the list (since list indices start at 0, we subtract 1 from k).
"""
<jupyter_output>
3
<jupyter_text>
Q1.2:
<jupyter_code>
"""
