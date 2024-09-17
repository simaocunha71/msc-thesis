def Split(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens