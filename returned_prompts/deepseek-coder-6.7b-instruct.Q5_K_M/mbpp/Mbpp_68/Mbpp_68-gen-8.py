def is_Monotonic(arr):
    return (all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))) or (all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1)))

print(is_Monotonic([6, 5, 4, 4]))  # True

"""
The function is_Monotonic takes an array arr as input. 
It checks if all the elements in the array satisfy the condition that each element is either less than or equal to the next one, or each element is greater than or equal to the next one.
If it does, it returns True; otherwise, it returns False.
"""

"""
This function works by iterating through the array from the first element to the second last element, and for each pair of elements, it checks if the current element is less than or equal to the next one, or the current element is greater than or equal to the next one.
The all function is used to check if all elements in the array satisfy the given condition.
"""

"""
In the example given, the array [6, 5, 4, 4] is monotonic, because each element is either less than or equal to the next one. So, the function returns True.
"""
<jupyter_output>
True
<jupyter_text>
Q2:
<jupyter_code>
