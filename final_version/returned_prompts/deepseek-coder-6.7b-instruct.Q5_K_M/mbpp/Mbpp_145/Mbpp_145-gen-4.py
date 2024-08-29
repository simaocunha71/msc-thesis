def max_Abs_Diff(arr):
    return max(abs(x-y) for x in arr for y in arr)

print(max_Abs_Diff((2,1,5,3))) # 4

"""
The function works by creating a list of all the absolute differences between any two elements in the array. It then returns the maximum value in that list.
"""

