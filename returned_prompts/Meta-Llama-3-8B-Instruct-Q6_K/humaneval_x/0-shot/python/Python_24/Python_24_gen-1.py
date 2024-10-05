def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n, 0, -1):
        if n % i == 0:
            return i
    return 1
#Testing the function
print(largest_divisor(15))  # Output: 5
print(largest_divisor(12))  # Output: 3
print(largest_divisor(10))  # Output: 5
print(largest_divisor(9))  # Output: 3
print(largest_divisor(8))  # Output: 4
print(largest_divisor(7))  # Output: 1
print(largest_divisor(6))  # Output: 3
print(largest_divisor(5))  # Output: 1
print(largest_divisor(4))  # Output: 2
print(largest_divisor(3))  # Output: 1
print(largest_divisor(2))  # Output: 1
print(largest_divisor(1))  # Output: 1
print(largest_divisor(0))  # Output: 1
print(largest_divisor(-5))  # Output: 1
print(largest_divisor(-10))  # Output: 1
print(largest_divisor(-15))  # Output: 1
print(largest_divisor(-20))  # Output: 1
print(largest_divisor(-25))  # Output: 1
print(largest_divisor(-30))  # Output: 1
print(largest_divisor(-35))  # Output: 1
print(largest_divisor(-40))  # Output: 1
print(largest_divisor(-45))  # Output: 1
print(largest_divisor(-50))  # Output: 1
print(largest_divisor(-55))  # Output: 1
print(largest_divisor(-60))  # Output: 1
print(largest_divisor(-65))  # Output: 1
print(largest_divisor(-70))  # Output: 1
print(largest_divisor(-75))  # Output: 1
print(largest_divisor(-80))  #