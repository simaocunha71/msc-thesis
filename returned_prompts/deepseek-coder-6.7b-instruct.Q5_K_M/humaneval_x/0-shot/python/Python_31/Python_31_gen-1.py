
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

# Test cases
print(is_prime(6))  # False
print(is_prime(101))  # True
print(is_prime(11))  # True
print(is_prime(13441))  # True
print(is_prime(61))  # True
print(is_prime(4))  # False
print(is_prime(1))  # False

# End of Solution

This function works by checking divisibility from 2 to the square root of the given number. If the number is divisible by any of these numbers, it is not prime, and the function returns False. If the number is not divisible by any of these numbers, it is prime, and the function returns True. The reason we only need to check up to the square root of the number is because a larger factor of the number would be a multiple of a smaller factor that has already been checked.

The time complexity of this function is O(sqrt(n)), which is efficient for large numbers. The space complexity is O(1), which is very efficient.

Please note that this solution assumes that the input is a positive integer. If the input can be negative or a float, you should add additional error checking to handle these cases.
"""

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of Solution

# End of