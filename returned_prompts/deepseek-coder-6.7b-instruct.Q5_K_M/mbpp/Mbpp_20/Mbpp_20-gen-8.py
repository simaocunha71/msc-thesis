
def is_woodall(n):
    num = str(n)
    product = 1
    for i in num:
        if i != '0':
            product *= int(i)
    return product == n


