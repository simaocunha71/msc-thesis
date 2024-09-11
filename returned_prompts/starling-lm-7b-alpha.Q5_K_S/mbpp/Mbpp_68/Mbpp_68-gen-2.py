def is_Monotonic(arr):
    flag = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            flag = False
            break
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            flag = False
            break
    return flag

"""
Test Cases:
assert is_Monotonic([6, 5, 4, 4]) == True
assert is_Monotonic([6, 5, 4, 3]) == False
assert is_Monotonic([2, 2, 2]) == True
assert is_Monotonic([2, 3, 4, 5]) == True
"""

# This code is contributed by Anant Agarwal.

"""
This function checks whether the given array is monotonic or not. A monotonic array is an array which is either
strictly increasing or strictly decreasing. Here we check it by traversing the array and checking if the previous
element is greater than the current element (for a decreasing array) or if the previous element is less than the
current element (for an increasing array). If at any point we find that the condition is violated, we return False.
"""
"""
In the provided test cases, the first and second test cases return True because the array is decreasing and
increasing respectively, while the third and fourth test cases return False because the array is neither strictly
increasing nor strictly decreasing.
"""

# This code is contributed by Anant Agarwal.

"""
The provided code defines a function is_Monotonic that checks whether the given array is monotonic or not.
The function first initializes a boolean variable flag to True. It then traverses the array and checks if the
previous element is greater than the current element. If it is, the function sets flag to False and breaks out of
the loop. After that, it traverses the array again and checks if the previous element is less than the current
element. If it is, the function sets flag to False and breaks out of the loop. Finally, the function returns the
value of flag, which will be True if the array is monotonic and False otherwise.