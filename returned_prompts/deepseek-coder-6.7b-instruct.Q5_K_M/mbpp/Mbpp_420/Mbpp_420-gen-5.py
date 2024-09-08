def cube_Sum(n):
    sum = 0
    num = 2
    for i in range(n):
        sum += num ** 3
        num += 2
    return sum

print(cube_Sum(2))

"""
Test Cases:
assert cube_Sum(2) == 72
assert cube_Sum(3) == 2192
assert cube_Sum(4) == 5832
assert cube_Sum(5) == 12544
"""

# Task 2:
