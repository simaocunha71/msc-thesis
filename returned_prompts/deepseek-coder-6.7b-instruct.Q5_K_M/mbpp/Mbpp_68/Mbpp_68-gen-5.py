def is_Monotonic(arr):
    if len(arr)<=2:
        return True
    else:
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))

print(is_Monotonic([6, 5, 4, 4]))  # True

"""
Explanation:

The function "is_Monotonic" takes an array as input.
If the length of the array is less than or equal to 2, it returns True as the array is already monotonic.

Otherwise, it checks whether the array is monotonic increasing by checking if all elements in the array are less than or equal to the next element.

If the above condition fails, it checks whether the array is monotonic decreasing by checking if all elements in the array are greater than or equal to the next element.

If either of the conditions is met, it returns True, else False.
"""

# Alternative Solution:

def is_Monotonic(arr):
    return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)) or
            all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))

print(is_Monotonic([6, 5, 4, 4]))  # True

"""
Explanation:

This function works in a similar manner to the previous one, but it does it in a more concise way by combining the two conditions into one line.

The conditions are the same as the previous function: either all elements are less than or equal to the next one (for increasing monotonicity), or all elements are greater than or equal to the next one (for decreasing monotonicity).
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2:
<jupyter_code>
