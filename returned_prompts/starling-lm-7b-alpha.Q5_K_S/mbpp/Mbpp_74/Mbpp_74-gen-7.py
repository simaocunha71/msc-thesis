def is_samepatterns(arr1, arr2):
    for i in range(len(arr1)-1):
        if arr1[i]!=arr1[i+1]:
            return False
        if arr2[i]!=arr2[i+1]:
            return False
    return True

# print(is_samepatterns(["red","green","green"], ["a", "b", "b"]))

"""
Write a function that takes in two arrays of numbers and returns a boolean indicating whether the two arrays are rotations of each other.

For example, if arr1 = [1, 2, 3] and arr2 = [3, 2, 1], the function should return True. If the two arrays are not rotations of each other, the function should return False.

Explanation:
If the lengths of the two arrays are not the same, the function should return False. Otherwise, the function should check if the arrays are rotations of each other by checking if the arrays are the same after each element in arr1 is moved to the right one position.
"""

def are_rotations(arr1, arr2):
    if len(arr1)!=len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i:]+arr1[:i]!=arr2:
            return False
    return True

# print(are_rotations([1, 2, 3], [3, 2, 1]))
# print(are_rotations([1, 2, 3, 4], [2, 3, 4, 1]))

"""
Write a function that takes in an array of integers and returns a boolean indicating whether the array is sorted in reverse order.

Explanation:
The function should return True if the array is sorted in reverse order, and False otherwise. To determine if an array is sorted in reverse order, the function should check if the difference between each pair of adjacent elements is greater than 0. If the difference between any pair of adjacent elements is less than or equal to 0, the function should return False.
"""

def is_reverse_sorted(arr):
    for i in range(len(arr)-1):