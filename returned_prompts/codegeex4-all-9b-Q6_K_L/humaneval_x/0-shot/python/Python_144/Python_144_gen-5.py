def simplify(x, n):
    x_numerator = int(x.split('/')[0])
    x_denominator = int(x.split('/')[1])
    n_numerator = int(n.split('/')[0])
    n_denominator = int(n.split('/')[1])
    return (x_numerator * n_numerator) % x_denominator == 0 and (x_denominator * n_denominator) % n_numerator == 0

print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False