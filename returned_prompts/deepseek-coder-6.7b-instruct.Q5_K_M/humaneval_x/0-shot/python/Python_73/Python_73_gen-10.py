
    # Initialize counters
    counter = 0
    # Initialize two pointers at the ends of the array
    start, end = 0, len(arr) - 1
    # While the start pointer is less than the end pointer
    while start < end:
        # If the elements at the start and end pointers are not the same
        if arr[start] != arr[end]:
            # Increment the counter
            counter += 1
        # Move the pointers towards the middle of the array
        start += 1
        end -= 1
    # Return the counter
    return counter

print(smallest_change([1,2,3,5,4,7,9,6])) # 4
print(smallest_change([1, 2, 3, 4, 3, 2, 2])) # 1
print(smallest_change([1, 2, 3, 2, 1])) # 0

"""
This code works by comparing the elements at the start and end of the array. If they are not equal, it increments a counter and moves the two pointers towards the middle of the array. This continues until the start pointer is no longer less than the end pointer. The counter is then returned as the minimum number of changes needed to make the array palindromic.
"""
<jupyter_output>
4
1
0
<jupyter_text>
10. Write a Python function that can perform a binary search on a sorted list. The function should return the index of the item being searched for or -1 if it's not present in the list.
<jupyter_code>
