def is_majority(arr, n, x):
    count = 0
    for i in range(n):
        if arr[i] == x:
            count += 1
    if count > n // 2:
        return True
    else:
        return False

print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3)) # True

"""
This function works by counting the number of occurrences of the element x in the array. If the count is greater than n/2, it returns True, otherwise it returns False.
"""
<jupyter_output>
True
<jupyter_text>
Problem 2
<jupyter_code>
