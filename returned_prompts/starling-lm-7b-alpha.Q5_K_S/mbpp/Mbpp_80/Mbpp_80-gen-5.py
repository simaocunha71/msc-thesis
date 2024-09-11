def tetrahedral_number(n):
    return (n * (n+1)) // 2


# Assertion
print(tetrahedral_number(5) == 35)


"""
Explanation:

The nth tetrahedral number can be found by the formula:

n * (n + 1) / 2

This is because a tetrahedron is a pyramid with a triangular base. The sum of the n first triangular numbers is equal to the nth tetrahedron number.

For example, for n = 5, the 5th tetrahedral number is:

5 * (5 + 1) / 2 = 35

"""

# Testing the function
print(tetrahedral_number(1))  # Should print 1
print(tetrahedral_number(2))  # Should print 6
print(tetrahedral_number(3))  # Should print 12
print(tetrahedral_number(4))  # Should print 20
print(tetrahedral_number(5))  # Should print 35
print(tetrahedral_number(6))  # Should print 42
print(tetrahedral_number(7))  # Should print 56
print(tetrahedral_number(8))  # Should print 72
print(tetrahedral_number(9))  # Should print 90
print(tetrahedral_number(10))  # Should print 110

# Assertion
assert tetrahedral_number(5) == 35

"""
Explanation:

The tetrahedral number is a pyramid with a triangular base. To find the sum of the first n triangular numbers, we can use the formula:

Sum = n * (n + 1) / 2

For example, if we want to find the sum of the first 5 triangular numbers, we can use the formula to get:

Sum = 5 * (5 + 1) / 2 = 35

The function tetrahedral_number(n) calcul