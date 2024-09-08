def split_Arr(arr, n):
    arr[:] = arr[n:] + arr[:n]
    return arr

print(split_Arr([12,10,5,6,52,36],2))

# This solution uses python's list slicing to split the list at the nth element and rearrange the list as required.
# The nth element is at the index 'n' and all elements after it are at the indexes less than 'n'.
# By slicing the list at 'n' and appending the first part to the end, we get the desired output.
# The list is updated in place (arr[:] = ...) to save memory.

# The time complexity of this solution is O(n) because slicing a list takes linear time.
# The space complexity is O(n) because a new list is created to hold the sliced elements.
<jupyter_output>
[5, 6, 52, 36, 12, 10]
<jupyter_text>
Question 3:
<jupyter_code>
