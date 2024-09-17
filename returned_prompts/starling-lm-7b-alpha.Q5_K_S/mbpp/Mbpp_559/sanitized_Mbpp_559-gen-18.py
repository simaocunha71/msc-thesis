def max_sub_array_sum(nums: list, size: int) -> int:
    n = len(nums)
    max_sum = 0
    for i in range(n):
        for j in range(i, i+size):
            if j >= n:
                break
            curr_sum = sum(nums[i:j+1])
            max_sum = max(max_sum, curr_sum)
    return max_sum