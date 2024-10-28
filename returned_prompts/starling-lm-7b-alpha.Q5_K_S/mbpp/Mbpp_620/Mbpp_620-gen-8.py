
def largest_subset(nums: list) -> int:
    nums.sort()
    prev = nums[0]
    count = 1
    for i in nums[1:]:
        if i % prev == 0:
            count += 1
            prev = i
    return count


