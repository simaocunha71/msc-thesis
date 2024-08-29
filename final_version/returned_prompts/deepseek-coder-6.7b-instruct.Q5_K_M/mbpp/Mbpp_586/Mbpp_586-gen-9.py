def split_Arr(arr, n):
    return arr[n:] + arr[:n]

print(split_Arr([12,10,5,6,52,36],2)) # Output: [5,6,52,36,12,10]

"""
This python function works by slicing the array at the nth element and then concatenating the two parts in reverse order.
"""

# 2.
