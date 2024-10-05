def simplify(x, n):
    from fractions import Fraction
    x = Fraction(x)
    n = Fraction(n)
    return x * n == int(x * n)

print(simplify("1/5", "5/1")) # True
print(simplify("1/6", "2/1")) # False
print(simplify("7/10", "10/2")) # False