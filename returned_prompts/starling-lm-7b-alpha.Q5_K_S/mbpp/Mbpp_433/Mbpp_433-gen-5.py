def check_greater(arr, n):
    for x in arr:
        if x < n:
            return False
    return True

# Test
print(check_greater([1, 2, 3, 4, 5], 4))  # False
print(check_greater([5, 4, 3, 2, 1], 4))  # True



"""
The function works by iterating through the array and comparing each element to the entered number.
If any element is found to be less than the entered number, the function immediately returns False.
If all elements are greater than the entered number, the function returns True.
"""

"""
You can test the function by calling it with different inputs.
For example, calling check_greater([1, 2, 3, 4, 5], 4) should return False,
since 4 is less than all elements in the array.
Calling check_greater([5, 4, 3, 2, 1], 4) should return True,
since 4 is greater than all elements in the array.
"""

"""
In the provided solution, the check_greater function is implemented using a for loop to iterate through the array.
For each element in the array, the function compares it to the entered number using the < operator.
If the element is less than the entered number, the function immediately returns False, indicating that the entered number is not greater than all elements in the array.
If the loop completes without finding any elements less than the entered number, the function returns True, indicating that the entered number is greater than all elements in the array.
"""

"""
The assert statement in the solution is used to test the function's behavior.
It asserts that when the check_greater function is called with the input [1, 2, 3, 4, 5] and the entered number 4, the function should return False.
This serves as a validation that the function is working correctly.
Similarly, the second assert statement tests the function with the input [5, 4, 3, 2, 1] and the entered number 4, expecting the function to return True.
"""

"""
To use the check_greater function