def multiply(a, b):
    return (a % 10) * (b % 10)  # Calculate the product of the unit digits of a and b. The % operator is used to get the remainder of the division, which is the unit digit of a number.  # return the product  # return (a % 10) * (b % 10)  # return the product

print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14,-15)) # should return 20

# Test cases
print(multiply(0,0)) # should return 0
print(multiply(123,456)) # should return 9
print(multiply(9999,9999)) # should return 9
print(multiply(-123,-456)) # should return 9
print(multiply(-123,456)) # should return 3

# Test edge cases
print(multiply(-0,0)) # should return 0
print(multiply(0,-0)) # should return 0
print(multiply(-0,-0)) # should return 0
print(multiply(0,0)) # should return 0

# Test cases with negative numbers
print(multiply(-123,456)) # should return 3
print(multiply(123,-456)) # should return 3
print(multiply(-123,-456)) # should return 9
print(multiply(123,456)) # should return 9

# Test cases with zero
print(multiply(0,0)) # should return 0
print(multiply(0,-456)) # should return 0
print(multiply(-456,0)) # should return 0
print(multiply(0,456)) # should return 0

# Test cases with large numbers
print(multiply(123456789,987654321)) # should return 9
print(multiply(-123456789,-987654321)) # should return 9
print(multiply(123456789,-987654321)) # should return 3
print(multiply(-123456789,987654321)) # should return 3

print(multiply(-123456789,-123456789)) # should return 9
print(multiply(123456789,