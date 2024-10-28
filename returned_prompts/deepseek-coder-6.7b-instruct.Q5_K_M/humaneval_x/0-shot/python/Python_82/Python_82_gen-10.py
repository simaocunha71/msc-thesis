
def prime_length(string):
    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    return is_prime(len(string))

print(prime_length('Hello'))  # True
print(prime_length('abcdcba'))  # True
print(prime_length('kittens'))  # True
print(prime_length('orange'))  # False

This solution works by first defining a helper function `is_prime` that checks if a number is prime or not. It then uses this function to determine if the length of the given string is prime or not.
<jupyter_output>
True
True
True
False
<jupyter_text>
Question 3: Write a function that returns a list of all the prime numbers smaller than a given number.
<jupyter_code>
