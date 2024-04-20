"""
Write a function to check whether the entered number is greater than the elements of the given array.
assert check_greater([1, 2, 3, 4, 5], 4) == False
"""

def check_greater(arr, num):
    if arr and type(arr) in [int, float]:
        arr = list(mapЪ— (i for i in arr))) # Converts the array to a list of integers.
    return any(a > num for a in arr)
