def second_smallest(nums):
    m1 = m2 = float('inf')
    for x in nums:
        if x <= m1:
            m1, m2 = x, m1
        elif x < m2:
            m2 = x
    return m2

print(second_smallest([1, 2, -8, -2, 0, -2]))

# Alternative solution:

def second_smallest(nums):
    nums.sort()
    for num in nums:
        if num > nums[0]:
            return num

print(second_smallest([1, 2, -8, -2, 0, -2]))

# Alternative solution:

def second_smallest(nums):
    return sorted(set(nums))[1]

print(second_smallest([1, 2, -8, -2, 0, -2]))

# Alternative solution:

def second_smallest(nums):
    return min(x for x in nums if x > min(nums))

print(second_smallest([1, 2, -8, -2, 0, -2]))

# Alternative solution:

def second_smallest(nums):
    return sorted(nums)[1]

print(second_smallest([1, 2, -8, -2, 0, -2]))

# Alternative solution:

def second_smallest(nums):
    m1 = min(nums)
    nums.remove(m1)
    m2 = min(nums)
    return m2

print(second_smallest([1, 2, -8, -2, 0, -2]))

# Alternative solution:

def second_smallest(nums):
    nums.remove(min(nums))
    return min(nums)

print(second_smallest([1, 2, -8, -2, 0, -2]))
"""
</code>
"""

# Alternative solution:

def second_smallest(nums):
