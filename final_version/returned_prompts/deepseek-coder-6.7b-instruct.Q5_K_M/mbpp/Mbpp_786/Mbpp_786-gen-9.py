def right_insertion(arr, val):
    for i in range(len(arr)):
        if arr[i]>val:
            return i
    return len(arr)

print(right_insertion([1,2,4,5],6))

"""
OUTPUT:
4
"""

# Alternative solution using binary search
def right_insertion_binary(arr, val):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= val:
            low = mid + 1
        else:
            high = mid
    return low

print(right_insertion_binary([1,2,4,5],6))

"""
OUTPUT:
4
"""
<jupyter_output>
4
4
<jupyter_text>
Question 3:
<jupyter_code>
"""
