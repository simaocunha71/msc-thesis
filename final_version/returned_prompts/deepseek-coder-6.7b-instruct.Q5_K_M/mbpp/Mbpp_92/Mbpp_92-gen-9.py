def is_undulating(n):
    s = str(n)
    return all(a != b for a, b in zip(s, s[1:]))

print(is_undulating(1212121))  # returns: True

Explanation:
The function `is_undulating` converts the number to a string and uses the `zip` function to pair each digit with the next one. It then uses the `all` function to check whether all pairs are not equal to each other.
"""

# Q2:
Q = """
Given a number, write a function to check whether the given number is a palindrome or not.
assert is_palindrome(121) == True
"""

# A2:
def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(121))  # returns: True

Explanation:
The function `is_palindrome` converts the number to a string and checks whether it is equal to its reverse. In Python, `s[::-1]` is a neat way to reverse a string.
"""

# Q3:
Q = """
Write a function to check whether a given number is a perfect number or not.
assert is_perfect(6) == True
"""

# A3:
def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

print(is_perfect(6))  # returns: True

Explanation:
The function `is_perfect` uses a generator comprehension to find all divisors of the number (excluding the number itself). It then checks whether the sum of these divisors is equal to the number itself. If so, the number is a perfect number.
"""

# Q4:
Q = """
Write a function to check whether the given number is a prime or not.
assert is_prime(5) == True
"""

# A4:
def is_prime(n):
    return all(n % i for i in range(2, int(n ** 0.5) + 1)) and