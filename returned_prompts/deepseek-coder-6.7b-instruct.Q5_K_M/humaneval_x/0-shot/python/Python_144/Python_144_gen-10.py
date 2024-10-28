
def simplify(x, n):
    # Convert x and n from string to int
    x_num, x_den = map(int, x.split('/'))
    n_num, n_den = map(int, n.split('/'))

    # Calculate the product of x and n
    product = x_num * n_num * (x_den * n_den)
    gcd = math.gcd(product, x_den * n_den)

    # Check if the product is a whole number
    if product // gcd == (x_num * n_num * x_den * n_den) // gcd:
        return True
    else:
        return False


print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False
print(simplify("2/3", "3/2"))  # True
print(simplify("1/1", "1/1"))  # True
print(simplify("1/2", "1/2"))  # True
print(simplify("1/2", "1/3"))  # False
print(simplify("1/4", "1/2"))  # True
print(simplify("1/4", "1/3"))  # False
print(simplify("1/10", "1/5"))  # False
print(simplify("3/7", "4/5"))  # True
print(simplify("1/6", "5/10"))  # True
print(simplify("1/4", "3/1"))  # True
print(simplify("1/4", "1/1"))  # True
print(simplify("1/3", "1/1"))  # True
print(simplify("1/2", "1/1"))  # True
print(simplify("1/1", "1/1"))  # True
print(simplify("1/8", "1/1"))  # True
