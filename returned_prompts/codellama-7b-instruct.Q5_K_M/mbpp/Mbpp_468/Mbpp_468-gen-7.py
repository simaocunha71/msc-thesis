"""
def max_product(arr):
    arr.sort()
    max_val = 1
    for i in range(len(arr)-1, -1, -1):
        max_val *= arr[i]
    return max_val
"""