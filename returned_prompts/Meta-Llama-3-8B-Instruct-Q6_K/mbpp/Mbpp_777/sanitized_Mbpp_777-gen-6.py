def find_sum(nums):
    return sum(i for i in set(nums) if list(nums).count(i) == 1)  # or sum(set([i for i in nums if nums.count(i) == 1]))