
def simplify(x, n):
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))
    return (x_num * n_den) % (x_den * n_num) == 0

print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False
print(simplify("1/2", "2/1"))  # True
print(simplify("1/2", "3/1"))  # False
print(simplify("1/2", "1/1"))  # True
print(simplify("3/4", "4/1"))  # True
print(simplify("1/1", "1/1"))  # True
print(simplify("1/6", "1/3"))  # True
print(simplify("1/2", "1/3"))  # False
print(simplify("1/4", "1/2"))  # True
print(simplify("1/2", "1/4"))  # False
print(simplify("1/3", "1/1"))  # True
print(simplify("1/4", "1/1"))  # True
print(simplify("1/1", "1/1"))  # True
print(simplify("1/8", "1/1"))  # True
print(simplify("1/1", "1/8"))  # True
print(simplify("1/1", "1/1"))  # True
print(simplify("1/5", "1/1"))  # True
print(simplify("1/1", "1/5"))  # True
print(simplify("1/1", "1/1"))  # True

"""
The function first splits the input fractions into numerator and denominator,
and then it checks if the result of multiplication of numerators is divisible by the product of