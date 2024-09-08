def is_majority(arr, n, x):
    for i in range(n):
        if arr[i] == x and arr[i + n//2] == x:
            return True
    return False

print(is_majority([1, 2, 3, 3, 3, 3, 10], 7, 3)) # True

"""
This function works by iterating over the array and checking if the element x appears in the array. It does so by checking if the element is equal to x and if the element in the array halfway in the array is also equal to x. If so, it returns True, indicating that the element is the majority element. If the function finishes iterating over the array without finding such an element, it returns False.
"""
<jupyter_output>
True
<jupyter_text>
Problem 2:
<jupyter_code>
