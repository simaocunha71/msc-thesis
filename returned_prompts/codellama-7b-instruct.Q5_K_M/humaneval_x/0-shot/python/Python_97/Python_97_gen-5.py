
def multiply(a, b):
    # Write your solution here
    a = str(a)
    b = str(b)
    product = 0
    for i in a:
        for j in b:
            product += int(i) * int(j)
    return product % 10



