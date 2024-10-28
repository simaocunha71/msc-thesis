def max_sub_array_sum_repeated(nums: list, k: int, times: int) -> int:
    return max(sum(nums[i:j+1] for j in range(k*times)) for i in range(k*times))