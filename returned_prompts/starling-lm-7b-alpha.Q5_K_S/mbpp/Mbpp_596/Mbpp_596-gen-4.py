def tuple_size(t):
    return sum(sys.getsizeof(x) for x in t)


"""
Write a function to count the number of times a given character appears in the given string.
assert count_char('Hello World', 'l') == 3
"""

B:
def count_char(s, c):
    return s.count(c)


"""
Write a function to check if a string is palindrome.
assert palindrome('racecar') == True
"""

C:
def palindrome(s):
    return s == s[::-1]


"""
Write a function to get the index of the first occurrence of the given substring in the given string.
assert find_str_index('Hello World', 'o') == 4
"""

D:
def find_str_index(s, c):
    return s.find(c)


"""
Write a function to check if a number is prime.
assert prime(7) == True
"""

E:
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


"""
Write a function to get the factorial of a number.
assert factorial(5) == 120
"""

F:
def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)


"""
Write a function to get the first n terms of the Fibonacci sequence.
assert fibonacci(5) == [1, 1, 2, 3, 5]
"""

G:
def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


"""
Write a function to calculate the sum of all divisors of a number.
assert sum_divisors(12)