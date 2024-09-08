"""
def max_sub_array_sum_repeated(arr, k, t):
    n = len(arr)
    max_sum = float('-inf')
    curr_sum = 0
    for i in range(n * k):
        curr_sum += arr[i % n]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum <= 0:
            curr_sum = 0
    return max_sum

print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))
"""

