def largest_subset(nums):
    nums = sorted(nums)
    max_size = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            size = 1
            num = nums[i]
            while num % 2 == 0:
                num //= 2
                size += 1
            if size > max_size:
                max_size = size
    return max_size