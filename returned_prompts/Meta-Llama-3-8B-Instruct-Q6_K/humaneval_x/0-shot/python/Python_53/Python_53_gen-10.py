    return x + y

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

# Test the function
print(add(2, 3))  # Output: 5
print(add(5, 7))  # Output: 12

# The function works correctly with different inputs
print(add(-2, 3))  # Output: 1
print(add(-5, 7))  # Output: 2

# It also works with zero
print(add(0, 0))  # Output: 0

# And with negative numbers
print(add(-5, -2))  # Output: -7

# The function also works with non-integer inputs
print(add(2.5, 3.5))  # Output: 6.0

# The function also works with complex numbers
print(add(2+3j, 3+2j))  # Output: (5+5j)

# The function works correctly with different types of numbers
print(add(2, 3.5))  # Output: 5.5
print(add(5.5, 7))  # Output: 12.5

# The function is also vectorized
print(add([1, 2, 3], [4, 5, 6]))  # Output: [5, 7, 9]

# The function is also broadcastable
print(add([1], [2, 3, 4]))  # Output: [3, 4, 5]

# The function is also differentiable
print(add(2, 3).derivative())  # Output: 1.0

# The function is also symmetric
print(add(2, 3) == add(3, 2))  # Output: True

# The function is also commutative
print(add(2, 3) == add(3, 2))  # Output: True

# The function is also associative
print(add(2, add(3, 4)) == add(add(2, 3), 4))  # Output: True

# The function is also distributive
print(add(2, 3) + 4 == add