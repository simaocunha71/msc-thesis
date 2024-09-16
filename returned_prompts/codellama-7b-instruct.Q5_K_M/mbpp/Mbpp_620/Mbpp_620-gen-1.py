
def largest_subset(nums):
    nums.sort()
    max_subset = 0
    for i, num in enumerate(nums):
        if num % nums[i+1] == 0:
            max_subset += 1
    return max_subset




