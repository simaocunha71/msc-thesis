def max_sub_array_sum(nums, target):
    curr_sum = 0
    curr_max = float('-inf')
    for num in nums:
        curr_sum += num
        curr_max = max(curr_max, curr_sum)
        if curr_sum < target:
            curr_sum = 0
    return curr_max


def max_sub_array_sum(nums, target):
    curr_max = float('-inf')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j+1]) > target:
                break
            curr_max = max(curr_max, sum(nums[i:j+1]))
    return curr_max


def max_sub_array_sum(nums, target):
    curr_max = float('-inf')
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum > target:
                break
            curr_max = max(curr_max, curr_sum)
    return curr_max


def max_sub_array_sum(nums, target):
    curr_max = float('-inf')
    for i in range(len(nums)):
        curr_sum = 0
        while i + curr_sum < len(nums) and curr_sum < target:
            curr_sum += nums[i + curr_sum]
        curr_max = max(curr_max, curr_sum)
    return curr_max


def max_sub_array_sum(nums, target):
    curr_max = float('-inf')
    for i in range(len(nums)):
        curr_sum = 0
        while i + curr_sum < len(nums) and curr_sum < target:
            curr_sum += nums[i + curr_sum]
        curr_max = max(curr_max, curr_sum)
    return curr_max
