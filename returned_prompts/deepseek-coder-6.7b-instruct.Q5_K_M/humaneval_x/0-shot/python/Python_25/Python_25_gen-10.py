from typing import List


def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while divisor <= n:
        if (n % divisor) == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return factors


print(factorize(8))
print(factorize(25))
print(factorize(70))


# The function works by continuously dividing the input number by a divisor until it can no longer be divided.
# The divisor is incremented until it can divide the number without a remainder.
# This process continues until the number has been fully factorized.
# The factors are then returned in a list from smallest to largest.

# The time complexity of this function is O(n), as it performs a single operation for each number from 2 to n.
# The space complexity is also O(n), as it stores a single number for each factor.

# The function does not return the number of times each factor appears in the factorization.
# The function also does not check if the input number is equal to the product of all factors.
# These additional checks would increase the complexity of the function.

# This function is not optimized for large input numbers.
# For large input numbers, a more efficient algorithm such as the Sieve of Eratosthenes or a modified version of the Sieve of Eratosthenes could be used.
# However, these algorithms are more complex and are not typically used for simple factorization problems.

# This function is a good starting point for understanding the basics of factorization and the process of finding prime factors.
# It is a good starting point for anyone interested in number theory or computer science.

# This function also serves as a good introduction to the concept of time complexity and space complexity.
# It shows how the time complexity can be measured in terms of the number of operations performed by the function.
# The space complexity can be measured in terms of the amount of memory used by the function.

# It's also a good example of how to write a function that uses a while loop to iterate until a certain condition is met.
# In this case, the condition is that the number has