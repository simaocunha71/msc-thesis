def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    def gcd(a, b):
        """Compute the greatest common divisor of a and b."""
        while b:
            a, b = b, a % b
        return a

    def simplify_fraction(frac):
        """Simplify a fraction."""
        num, denom = map(int, frac.split('/'))
        common_divisor = gcd(num, denom)
        return f'{num // common_divisor}/{denom // common_divisor}'

    return simplify_fraction(x + '/' + n) == '1/1'

print(simplify("1/5", "5/1")) # True
print(simplify("1/6", "2/1")) # False
print(simplify("7/10", "10/2")) # False
print(simplify("1/5", "1/5")) # True
print(simplify("2/7", "3/8")) # False
print(simplify("3/9", "2/6")) # True
print(simplify("4/12", "3/6")) # True
print(simplify("5/15", "4/12")) # True
print(simplify("6/18", "5/15")) # False
print(simplify("7/21", "6/18")) # False