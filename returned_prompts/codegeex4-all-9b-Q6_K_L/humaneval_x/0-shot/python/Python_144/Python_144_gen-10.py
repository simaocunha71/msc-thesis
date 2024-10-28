def simplify(x, n):
    numerator = int(x.split('/')[0])
    denominator = int(x.split('/')[1])
    numerator *= int(n.split('/')[0])
    denominator *= int(n.split('/')[1])
    return numerator % denominator == 0

print(simplify("1/5", "5/1")) # True
print(simplify("1/6", "2/1")) # False
print(simplify("7/10", "10/2")) # False