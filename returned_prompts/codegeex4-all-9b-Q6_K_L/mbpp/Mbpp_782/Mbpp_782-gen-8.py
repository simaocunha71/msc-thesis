def odd_length_sum(nums):
    sum = 0
    for i in range(len(nums)):
        if len(nums[i:]) % 2 != 0:
            sum += sum(nums[i:])
    return sum

