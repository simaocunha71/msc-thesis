def find_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    lucas_nums = [2, 1]
    for i in range(2, n+1):
        lucas_nums.append(lucas_nums[i-1] + lucas_nums[i-2])
    return lucas_nums[n]

print(find_lucas(9))

# 2.
"""
Write a function to find the n'th fibonacci number.
assert find_fibonacci(9) == 34
"""

def find_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibonacci_nums = [0, 1]
    for i in range(2, n+1):
        fibonacci_nums.append(fibonacci_nums[i-1] + fibonacci_nums[i-2])
    return fibonacci_nums[n]

print(find_fibonacci(9))

# 3.
"""
Write a function to find the factorial of a number.
assert find_factorial(5) == 120
"""

def find_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial

print(find_factorial(5))

# 4.
"""
Write a function to find the n'th harmonic number.
assert find_harmonic_number(5) == 2.525
"""

def find_harmonic_number(n):
    harmonic_number = 0
    for i in range(1, n+1):
        harmonic_number += 1/i
    return harmonic_number

print(find_harmonic_number(5))

# 5.
"""
Write a function to find the n'th triangular number.
assert find_triangular