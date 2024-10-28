
def multiply(a, b):
    return (abs(a) % 10) * (abs(b) % 10)


print(multiply(148, 412))  # should return 16
print(multiply(19, 28))  # should return 72
print(multiply(2020, 1851))  # should return 0
print(multiply(14, -15))  # should return 20


#  The function takes two integers a and b. It returns the product of the unit digits of a and b.
#  The unit digits are the rightmost digit of a number.
#  To get the unit digit of a number we take modulo 10 of the absolute value of the number.
#  The modulo operator returns the remainder of the division of the number by 10.
#  We multiply the unit digits of a and b and return the result.
#  To get the unit digit of b we use abs(b) % 10. The modulo operator returns the remainder of the division of b by 10.
#  If b is negative, abs(b) % 10 will give the unit digit of its positive counterpart.
#  If b is positive, abs(b) % 10 will give the unit digit of b.
#  We do the same for a.
#  We use abs function to ensure that we get the unit digit of the number even if it is negative.
#  If the number is negative, the modulo operator will give the unit digit of its positive counterpart.
#  If the number is positive, the modulo operator will give the unit digit of the number.
#  We multiply the unit digits of a and b and return the result.
#  The result is the product of the unit digits of a and b.
#  If the product is zero, it means that at least one of the numbers has a unit digit of zero.
#  If the product is not zero, it means that both numbers have non-zero unit digits.
#  The product of the unit digits of two numbers is the product of the digits that they represent.