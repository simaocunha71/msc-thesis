def is_Monotonic(arr):
    if len(arr) == 1:
        return True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

# print(is_Monotonic([6, 5, 4, 4]))
# print(is_Monotonic([5, 4, 4, 4, 4, 4, 4, 4, 5, 4]))
# print(is_Monotonic([5, 4, 4, 4, 4, 4, 4, 4, 4, 5]))
# print(is_Monotonic([1, 2, 3, 4, 5]))
# print(is_Monotonic([5, 4, 3, 2, 1]))

"""
Write a python function to check whether the given array is monotonic or not.
assert is_Monotonic([6, 5, 4, 4]) == True
"""

def is_Monotonic(arr):
    if len(arr) == 1:
        return True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

# print(is_Monotonic([6, 5, 4, 4]))
# print(is_Monotonic([5, 4, 4, 4, 4, 4, 4, 4, 4, 5]))
# print(is_Monotonic([5, 4, 4, 4, 4, 4, 4, 4, 4, 5]))
# print(is_Monotonic([1, 2, 3, 4, 5]))
# print(is_Monotonic([5, 4, 3, 2, 1]))

def is_Monotonic(arr):
    if len(arr) == 1:
        return True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1