
    primes = []
    for i in lst:
        if is_prime(i):
            primes.append(i)
    if primes:
        return sum(map(int, str(max(primes))))
    else:
        return 0


def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# This solution uses the Python builtin function max() to find the largest prime value in the list
# and then uses the builtin sum() function to sum up the digits of that number.

# The is_prime() function is a simple function that checks if a number is a prime number.

# Note that the function is_prime() does not actually check if the number is prime. 
# The function is_prime() is a simple function that checks if a number is a prime number. 
# It only checks if the number is a prime number if it is greater than 1, 
# and it checks if the number is a prime number by iterating over all numbers from 2 to the square root of the number. 
# If it finds a number that divides the number without leaving a remainder, it returns False. 
# If it does not find a number that divides the number without leaving a remainder, it returns True.

# The solution is a simple solution that uses two builtin functions to find the largest prime number in a list of numbers.