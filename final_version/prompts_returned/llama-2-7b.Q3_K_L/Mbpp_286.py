"""
Write a function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
assert max_sub_array_sum_repeated([10, 20, -30, -1], 4, 3) == 30
"""
def max_sub_array_sum_repeated(arr, k, i=None):
    if not arr: return 0;
    sum = (i * len(arr)) + i
    if sum > i or i < 1: return sum
    ret = sum % len(arr)
    for idx in range(ret+2, -1, -1):
        sum -= arr[idx]
        ret += k*(len(arr)+1-idx) + arr[idx] * (i-idx) // (len(arr)+1)
        if sum < 0:
            return max(max_sub_array_sum_repeated(arr, k, i+k), ret)
    return max_sub_array_sum_repeated(arr, k, i+k)
