def big_sum(nums):
    # Code here
    return max(nums) + min(nums)

# Tests
print(big_sum([1, 2, 3]) == 4)




def big_sum(nums):
    # Code here
    return max(nums) + min(nums)

# Tests
print(big_sum([1, 2, 3]) == 4)


"""
def big_sum(nums):
    # Code here
    return sum(nums) - min(nums) - max(nums)

# Tests
print(big_sum([1, 2, 3]) == 4)
"""

"""
def big_sum(nums):
    # Code here
    return sum(nums[:-1]) + nums[-1]

# Tests
print(big_sum([1, 2, 3]) == 4)
"""

"""
def big_sum(nums):
    # Code here
    return sum(nums[:-1]) + nums[0]

# Tests
print(big_sum([1, 2, 3]) == 4)
"""

"""
def big_sum(nums):
    # Code here
    return sum(nums[1:]) + nums[0]

# Tests
print(big_sum([1, 2, 3]) == 4)
"""

"""
def big_sum(nums):
    # Code here
    return sum(nums[:-1]) + sum(nums[1:])

# Tests
print(big_sum([1, 2, 3]) == 4)
"""

"""
def big_sum(nums):
    # Code here
    return sum(nums[:-1]) + sum(nums[1:]) + nums[0]

# Tests
print(big_sum([1, 2, 3]) == 4)
"""

"""
def big_sum(nums):
    # Code here
    return sum(nums[:-1]) + sum(nums[1:])