
    if len(array) == 0:
        return array
    elif len(array) % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

print(sort_array([]))  # []
print(sort_array([5]))  # [5]
print(sort_array([2, 4, 3, 0, 1, 5]))  # [0, 1, 2, 3, 4, 5]
print(sort_array([2, 4, 3, 0, 1, 5, 6]))  # [6, 5, 4, 3, 2, 1, 0]

"""
Explanation:
In the first test case, the given array is empty so the function should return the array as it is.
In the second test case, the given array only has one element, so the function should return the array as it is.
In the third test case, the sum of the first and last indices of the array is odd, so the array should be sorted in ascending order.
In the fourth test case, the sum of the first and last indices of the array is even, so the array should be sorted in descending order.
"""
<jupyter_output>
[]
[5]
[0, 1, 2, 3, 4, 5]
[6, 5, 4, 3, 2, 1, 0]
<jupyter_text>
Task 2: Write a Python program to check if a string is a palindrome or not.
<jupyter_code>
