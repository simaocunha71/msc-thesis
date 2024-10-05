def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return reduce(lambda x, y: x * y if y % 2 else x, [int(i) for i in str(n)], 1)

print(digits(1))  # == 1
print(digits(4))  # == 0
print(digits(235))  # == 15
print(digits(1234567890))  # == 15
print(digits(1111))  # == 0
print(digits(2222222222))  # == 0
print(digits(6666666666))  # == 0
print(digits(4999999999))  # == 331776

def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return reduce(lambda x, y: x * y if y % 2 else x, [int(i) for i in str(n)], 1)

print(digits(1))  # == 1
print(digits(4))  # == 0
print(digits(235))  # == 15
print(digits(1234567890))  # == 15
print(digits(1111))  # == 0
print(digits(2222222222))  # == 0
print(digits(6666666666))  # == 0
print(digits(4999999999))  # == 331776