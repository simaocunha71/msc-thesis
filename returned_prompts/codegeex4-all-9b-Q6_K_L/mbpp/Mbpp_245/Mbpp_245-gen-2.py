def max_sum(nums: list) -> int:
    max_sum = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if is_bitonic(nums[i:j+1]):
                max_sum = max(max_sum, sum(nums[i:j+1]))
    return max_sum

def is_bitonic(nums: list) -> bool:
    if len(nums) < 2:
        return False
    increasing = nums[0] < nums[1]
    for i in range(1, len(nums)-1):
        if (nums[i] < nums[i+1]) != increasing:
            return False
    return True

# Test the function
print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9])) # Output: 194

