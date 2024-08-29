
def find_lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    lucas_numbers = [2, 1]
    for i in range(2, n+1):
        lucas_numbers.append(lucas_numbers[-1] + lucas_numbers[-2])
    return lucas_numbers[-1]

print(find_lucas(9))  # 76

"""
Write a function that takes a number and returns whether or not that number is a prime.
assert is_prime(7) == True
assert is_prime(10) == False
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(7))  # True
print(is_prime(10))  # False

"""
Write a function that returns the n'th fibonacci number.
assert find_fibonacci(9) == 34
"""

def find_fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    fibonacci_numbers = [0, 1]
    for i in range(2, n+1):
        fibonacci_numbers.append(fibonacci_numbers[-1] + fibonacci_numbers[-2])
    return fibonacci_numbers[-1]

print(find_fibonacci(9))  # 34

"""
Write a function that takes a list of numbers and returns the median of those numbers.
assert find_median([5, 2, 9, 1, 5, 6]) == 5
assert find_median([1, 1, 2