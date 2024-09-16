def find_max_subarray(arr):
    if len(arr) == 1:
        return arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        max_sum = max(max_sum, max_sum + arr[i])
    return max_sum

"""
Write a function to find the maximum sum of a subarray in the given array. 
arr = [1, 2, 3, 4, 5]
assert find_max_subarray([1, 2, 3, 4, 5]) == 15
