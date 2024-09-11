def pair_wise(nums):
    result = []
    for i in range(len(nums)-1):
        result.append((nums[i],nums[i+1]))
    return result

# Tests
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
assert pair_wise([1,2,3])==[(1, 2), (2, 3)]


"""
Optimized solution

def pairwise(nums):
    return zip(nums[::2],nums[1::2])

assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
assert pair_wise([1,2,3])==[(1, 2), (2, 3)]

"""



# Other solution
"""
def pairwise(nums):
    result = []
    for i in range(len(nums)-1):
        result.append((nums[i],nums[i+1]))
    return result

# Tests
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
assert pair_wise([1,2,3])==[(1, 2), (2, 3)]

"""


"""
def pairwise(nums):
    result = []
    for i in range(len(nums)):
        result.append((nums[i],nums[i+1]))
    return result

# Tests
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1),