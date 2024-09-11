def pos_count(nums):
    count = 0
    for i in nums:
        if i > 0:
            count += 1
    return count

# Test the function
assert pos_count([1,-2,3,-4]) == 2

# More test cases
assert pos_count([1, 2, 3]) == 3
assert pos_count([-1, 0, 3, 4, 5]) == 3
assert pos_count([0, -1, -2]) == 0

# Add some negative numbers
assert pos_count([-1, -2, -3]) == 0
assert pos_count([-1, -2, -3, -4]) == 0

# Add some zeroes
assert pos_count([0, -1, 0, 2, -3]) == 2
assert pos_count([0, -1, 0, 2, 3, -3]) == 3

# Add some more numbers
assert pos_count([-1, 0, 1, -2, 3, 0, 4, -3]) == 4

# Add some very large numbers
assert pos_count([10**100, 2*10**100]) == 2
assert pos_count([-10**100, 10**100, 2*10**100]) == 2

# Add some very small numbers
assert pos_count([-10**-100, 10**-100, 2*10**-100]) == 2
assert pos_count([-10**-100, -10**-100, 10**-100]) == 1

# Add some zeroes and negative numbers
assert pos_count([0, -10**-100, 0, 10**-100]) == 1

# Add some negative numbers and zeroes
assert pos_count([-10**-100, 0, -10**-100, 0]) == 0

# Add some positive numbers