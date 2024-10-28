def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 1
    odd = False
    for i in str(n):
        if int(i) % 2 == 1:
            odd = True
            result *= int(i)
    return result if odd else 0

print(digits(1))  # 1
print(digits(4))  # 0
print(digits(235))  # 15
print(digits(246))  # 0
print(digits(13579))  # 315