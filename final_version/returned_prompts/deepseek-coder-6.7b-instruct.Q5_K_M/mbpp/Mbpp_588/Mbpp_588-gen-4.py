def big_diff(nums):
    return max(nums) - min(nums)

print(big_diff([1,2,3,4]))

# Alternate Solution
def big_diff(nums):
    max_num = nums[0]
    min_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num - min_num

print(big_diff([1,2,3,4]))

# Alternate Solution
def big_diff(nums):
    max_num = nums[0]
    min_num = nums[0]
    for i in range(len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]
        if nums[i] < min_num:
            min_num = nums[i]
    return max_num - min_num

print(big_diff([1,2,3,4]))

