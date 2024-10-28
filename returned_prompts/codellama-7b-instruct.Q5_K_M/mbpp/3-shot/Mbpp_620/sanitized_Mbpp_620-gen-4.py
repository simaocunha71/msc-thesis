def largest_subset(nums: list) -> int:
    largest = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0:
                largest = max(largest, j-i+1)
    return largest