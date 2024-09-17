
def largest_subset(nums: list) -> int:
    nums.sort()
    max_size = 0
    curr_size = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            curr_size += 1
        else:
            if curr_size > max_size:
                max_size = curr_size
            curr_size = 1
    if curr_size > max_size:
        max_size = curr_size
    return max_size


