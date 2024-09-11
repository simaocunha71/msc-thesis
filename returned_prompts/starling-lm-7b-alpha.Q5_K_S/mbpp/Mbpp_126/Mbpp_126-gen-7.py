"""
def sum_common_divisors(a,b):
    c = 1
    d = min(a,b)
    while c <= d:
        if a%c == 0 and b%c == 0:
            sum = c + sum_common_divisors(a,b,c+1)
        c += 1
    return sum

assert sum_common_divisors(10,15) == 6
"""

def sum_common_divisors(a,b):
    c = 1
    d = min(a,b)
    while c <= d:
        if a%c == 0 and b%c == 0:
            sum = c + sum_common_divisors(a,b,c+1)
        c += 1
    return sum

assert sum_common_divisors(10,15) == 6

# Sum of common divisors of 10 and 15 is 6
# Sum of common divisors of 24 and 36 is 36
# Sum of common divisors of 8 and 27 is 24
# Sum of common divisors of 16 and 25 is 1
# Sum of common divisors of 12 and 18 is 6
# Sum of common divisors of 20 and 24 is 12
# Sum of common divisors of 12 and 18 is 6
# Sum of common divisors of 20 and 30 is 10
# Sum of common divisors of 48 and 60 is 36
# Sum of common divisors of 40 and 72 is 24
# Sum of common divisors of 100 and 120 is 120
# Sum of common divisors of 100 and 125 is 50
# Sum of common divisors of 120 and 150 is 120
# Sum of common divisors of 100 and 150 is 100
# Sum of common divisors of 100 and 175 is 50
#