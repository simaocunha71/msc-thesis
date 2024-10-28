def largest_subset(nums):
    '''
    Given a list of numbers, find the size of the largest subset so that every pair is divisible.
    '''
    max_size = 0
    for num in nums:
        # Check if the number is divisible by 2
        if num % 2 == 0:
            max_size += 1
        else:
            if max_size > 0:
                max_size = 0
    return max_size