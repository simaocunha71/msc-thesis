def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    odd_found = False
    for digit in str(n):
        if int(digit) % 2 != 0:
            product *= int(digit)
            odd_found = True
    return product if odd_found else 0

print(digits(1))  # 1
print(digits(4))  # 0
print(digits(235))  # 15
print(digits(3245))  # 0
print(digits(3265))  # 30
print(digits(0))  # 0
print(digits(2))  # 0
print(digits(1345))  # 45
print(digits(9))  # 9
print(digits(13457))  # 315