
def max_sub_array_sum_repeated(arr, k, t):
    # calculate the total sum of array
    total_sum = sum(arr)

    # calculate the sum of array multiplied by k
    k_sum = total_sum * k

    # calculate the length of array multiplied by k
    n = len(arr) * k

    # calculate the maximum sum of subarray
    max_sum = kadanes(arr, n, k_sum)

    return max_sum

def kadanes(arr, n, k_sum):
    max_sum = float('-inf')
    cur_sum = 0

    for i in range(n):
        cur_sum = cur_sum + arr[i % len(arr)]
        if cur_sum > max_sum:
            max_sum = cur_sum

        if cur_list_sum < 0:
            cur_list_sum = 0

    return max_sum

print(max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3))  # 30
"""
Explanation:

The array is [10, 20, -30, -1] and it is repeated 4 times. So the modified array becomes [10, 20, -30, -1, 10, 20, -30, -1, 10, 20, -30, -1, 10, 20, -30, -1].
The sum of this array is 16 and the sum of this array repeated 3 times is 48. The maximum sum of the subarray of this repeated array is 30.
"""

