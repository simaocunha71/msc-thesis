def Split(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result

