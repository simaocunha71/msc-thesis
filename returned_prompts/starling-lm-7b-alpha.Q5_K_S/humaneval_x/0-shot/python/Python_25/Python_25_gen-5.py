    factors = []
    div = 2
    while n > 1:
        while n % div == 0:
            factors.append(div)
            n //= div
        div += 1
    factors.sort()
    return factors


# Testing
print(factorize(8))
print(factorize(25))
print(factorize(70))


# Created by: Madi Saidov
# Date: 09.06.2020


# To check factorization of an integer, we can divide it by the smallest prime
# numbers starting from 2. If the division is possible without any remainder,
# we've found a factor. We add it to the result list and divide the number
# repeatedly by this factor until the result of the division is 0. Then we
# move to the next smallest prime number.

# We start the process with the smallest prime number, 2, and continue with
# the next smallest prime number if the division by the previous one was possible
# without any remainder. We continue this process until the number becomes 1,
# which means that the number has been divided by all its factors.

# The result is a list of factors of the number in the order from smallest to largest.
# Each of the factors is listed as many times as it appears in the factorization.

# Here are some examples of the function's usage:

# factorize(8) returns [2, 2, 2] because 8 = 2 * 2 * 2
# factorize(25) returns [5, 5] because 25 = 5 * 5
# factorize(70) returns [2, 5, 7] because 70 = 2 * 5 * 7

# Time complexity: O(sqrt(n)) because the biggest prime factor of any number
# is less or equal to the square root of that number

# This function is implemented in Python, which means that it is relatively
# slow compared to other languages like C++. However, the function is very
# easy to use and understand, which makes it suitable for educational purposes.

# In Python, you can define the function like this:

# from typing import List