
    if len(lst) == 0:
        return 0
    
    return sum([i**2 if i%2 != 0 and i >= 0 else 0 for i in lst])

# Test cases:
print(double_the_difference([1, 3, 2, 0]))  # 10
print(double_the_difference([-1, -2, 0]))  # 0
print(double_the_difference([9, -2]))  # 81
print(double_the_difference([0]))  # 0
print(double_the_difference([]))  # 0

"""

def double_the_difference(lst):
    return sum([i**2 for i in lst if i%2 != 0 and i >= 0]) if lst else 0

# Test cases:
print(double_the_difference([1, 3, 2, 0]))  # 10
print(double_the_difference([-1, -2, 0]))  # 0
print(double_the_difference([9, -2]))  # 81
print(double_the_difference([0]))  # 0
print(double_the_difference([]))  # 0

"""

"""
def double_the_difference(lst):
    return sum(i**2 for i in lst if isinstance(i, int) and i < 0)
"""

"""
def double_the_difference(lst):
    return sum(i**2 if i%2 != 0 else 0 for i in lst if isinstance(i, int) and i >= 0)
"""

"""
def double_the_difference(lst):
    return sum(i**2 if isinstance(i, int) and i%2 != 0 and i >= 0 else 0 for i in lst)
"""

"""
def double_the_difference(lst):
    return sum(i**2 for i in lst if i%2 != 0 and isinstance(i, int) and i >= 0)
"""

"""