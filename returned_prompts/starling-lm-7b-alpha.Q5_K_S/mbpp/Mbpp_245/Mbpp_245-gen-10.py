def max_sum(arr):
    if len(arr) <= 2:
        return max(arr)

    max_left = [0] * len(arr)
    max_right = [0] * len(arr)

    max_left[0] = arr[0]
    max_right[-1] = arr[-1]

    for i in range(1, len(arr)):
        max_left[i] = max(max_left[i-1], arr[i])
        for j in range(i-2, -1, -1):
            max_left[i] = max(max_left[i], arr[j] + max_left[j])

    for i in range(len(arr) - 2, -1, -1):
        max_right[i] = max(max_right[i+1], arr[i])
        for j in range(i+2, len(arr)):
            max_right[i] = max(max_right[i], arr[j] + max_right[j])

    return max(max_left[-1], max_right[0])

# assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194

"""
"""

# Time complexity: O(N^2)
# Space complexity: O(N)

# This solution is based on the concept of dynamic programming.
# We use two arrays, max_left and max_right, to store the maximum sum of subsequences that end at each position in the array.
# We initialize max_left and max_right with the first and last element of the array, respectively.
# Then, we iterate through the array and update the max_left and max_right arrays accordingly.
# Finally, we return the maximum value between the maximum sum of the left and right subsequences.

# This solution has a time complexity of O(N^2) because we need to iterate through the array twice.
# The space complexity is O(N) because we need to store the max_left and max_right arrays, which have a size of