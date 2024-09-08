
def max_sub_array_sum_repeated(arr: list, k: int, t: int) -> int:
    # get the maximum sub array sum
    def kadane(arr):
        max_current = max_global = arr[0]
        for i in range(1, len(arr)):
            max_current = max(arr[i], max_current + arr[i])
            if max_current > max_global:
                max_global = max_current
        return max_global

    n = len(arr)
    arr_repeated = arr * k
    max_sum = 0

    for i in range(n):
        for j in range(i + n, len(arr_repeated)):
            if j - i + 1 > n * t:
                continue
            max_sum = max(max_sum, kadane(arr_repeated[i:j + 1]))

    return max_sum

print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))

"""
This program is using Kadane's algorithm to find the maximum sub array sum in an array. The maximum sub array sum is calculated by iterating over the array and updating the maximum current sum and the maximum global sum at each index. The time complexity of this approach is O(n), where n is the length of the array.
"""

#Time complexity: O(n^2)
#Space complexity: O(n)

#Test cases:
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
assert max_sub_array_sum_repeated([-1, -2, -3, -4], 4, 2) == -1
assert max_sub_array_sum_repeated([1, 2, 3, 4], 4, 1) == 10
assert max_sub_array_sum_repeated([-2, 1, -3, 4, -1, 2, 1, -5,