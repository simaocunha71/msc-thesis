"""
def all_unique(nums):
    return len(set(nums)) == len(nums)

# Test
assert all_unique([1,2,3]) == True

"""

def all_unique(nums):
    return len(set(nums)) == len(nums)

# Test
assert all_unique([1,2,3]) == True

# Test
assert all_unique([1,1,2,3]) == False

# Test
assert all_unique([]) == True

# Test
assert all_unique([1]) == True

# Test
assert all_unique([1,2]) == True


# Test
assert all_unique([1,2,2]) == False

# Test
assert all_unique([1,1,1,1]) == False

# Test
assert all_unique([1,1,1,1,1]) == False

# Test
assert all_unique([1,1,1,1,1,1]) == False

# Test
assert all_unique([1,1,1,1,1,2]) == False

# Test
assert all_unique([1,2,3,4]) == True

# Test
assert all_unique([1,2,3,3]) == False

# Test
assert all_unique([1,2,3,3,4]) == False

# Test
assert all_unique([1,2,3,3,4,4]) == False

# Test
assert all_unique([1,2,3,3,4,4,5]) == False

# Test
assert all_unique([1,2,3,3,4,4,5,5]) == False

# Test
assert all_unique([1,2,3,3,4,4,5,5,6]) == False

# Test
assert all_unique([1,2,3,3,4,4,5,5,6,6]) == False

# Test
assert all_unique([1,2,3,3,4,4,5,5,6,6,7]) == False

# Test
assert all_unique([1,2