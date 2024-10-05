
def digits(n):
    product = 0
    for digit in str(n):
        if int(digit) % 2 == 1:
            product *= int(digit)
        else:
            product = 0
    return product
