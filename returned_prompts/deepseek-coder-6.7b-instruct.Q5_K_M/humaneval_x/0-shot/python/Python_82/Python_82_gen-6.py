
    def is_prime(n):
        """helper function to check if a number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    return is_prime(len(string))


print(prime_length('Hello'))  # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))  # True
print(prime_length('orange'))  # False

```

The `is_prime` helper function checks if a given number `n` is a prime number by iterating from 2 to the square root of `n` and checking if `n` is divisible by any of these numbers. If it is, then `n` is not prime and the function returns False. If `n` is not divisible by any of these numbers, then it is prime and the function returns True.

The main function `prime_length` takes a string as input, calculates its length with `len(string)`, and checks if this length is a prime number by calling the `is_prime` function. It returns True if the length is prime and False otherwise.

This solution works by checking if the length of the input string is prime and returns True if it is and False if it's not.

This solution has a time complexity of O(sqrt(n)) as it checks for divisibility up to the square root of the number. The space complexity is O(1) as it only uses a constant amount of space to store the input string and the result of its length.
"""

def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    def is_prime(n):
        """helper function to check if a number is prime"""
        if n < 2:
            return False
        for i in range