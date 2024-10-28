def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    odds = [int(i) for i in str(n) if int(i) % 2 != 0]
    if len(odds) == 0:
        return 0
    else:
        return reduce(lambda x, y: x * y, odds)

print(digits(1))  == 1
print(digits(4))  == 0
print(digits(235)) == 15
print(digits(8)) == 0
print(digits(0)) == 0
print(digits(123456789)) == 945
print(digits(11111111111111)) == 1

# Note: This is a very simple solution and does not account for large numbers.
# For example, digits(123456789123456789123456789) will return 945, not 945378647578945378647578945.