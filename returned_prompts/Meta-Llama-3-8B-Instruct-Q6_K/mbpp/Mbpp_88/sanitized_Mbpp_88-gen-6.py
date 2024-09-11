def freq_count(nums):
    return {num: nums.count(num) for num in set(nums)}