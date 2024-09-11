from math import sqrt, ceil
def next_Perfect_Square(n):
    while True:
        if int(ceil(sqrt(n)))**2 == n+1:
            return n+1
        n += 1

# Testing
print(next_Perfect_Square(35))  # Expected output: 36

# Testing with edge cases
print(next_Perfect_Square(0))  # Expected output: 1
print(next_Perfect_Square(1))  # Expected output: 4
print(next_Perfect_Square(2))  # Expected output: 9
print(next_Perfect_Square(3))  # Expected output: 4
print(next_Perfect_Square(4))  # Expected output: 9
print(next_Perfect_Square(5))  # Expected output: 9
print(next_Perfect_Square(6))  # Expected output: 25
print(next_Perfect_Square(7))  # Expected output: 25
print(next_Perfect_Square(8))  # Expected output: 25
print(next_Perfect_Square(9))  # Expected output: 25
print(next_Perfect_Square(10))  # Expected output: 25














"""
Write a python function to find the next perfect square greater than a given number.

Explanation:
The function first calculates the square root of the given number, rounds it up to the nearest integer using the ceil() function, and then squares the result. If the square of the rounded number is equal to the given number plus one, the function returns the given number plus one as the next perfect square. Otherwise, the function increments the given number by one and repeats the process until a perfect square is found.

Test Cases:
- next_Perfect_Square(35) == 36
- next_Perfect_Square(0) == 1
- next_Perfect_Square(1) == 4
- next_