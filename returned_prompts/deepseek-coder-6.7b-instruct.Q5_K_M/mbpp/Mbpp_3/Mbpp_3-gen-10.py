def is_not_prime(n):
    if n < 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

assert is_not_prime(2) == False
assert is_not_prime(3) == False
assert is_not_prime(4) == True
assert is_not_prime(9) == True
assert is_not_prime(15) == True
assert is_not_prime(21) == True
assert is_not_prime(25) == True
assert is_not_prime(73) == False
assert is_not_prime(100) == True
assert is_not_prime(101) == False
"""
The function works by checking if a number is less than 2 (the smallest prime number). If it is, it returns True because non-prime numbers are less than 2. If the number is 2 or greater, it checks if there are any numbers from 2 to the square root of the number that can divide the number evenly. If there are, the number is not prime and the function returns True. If there are not, the number is prime and the function returns False.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
1.3.2: Prime factorizationWrite a python function to calculate the prime factorization of a given number. Your function should return a list of tuples, where each tuple contains a prime number and its corresponding exponent.
<jupyter_code>
