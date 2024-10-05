
def multiply(a, b):
    a = str(a)
    b = str(b)
    res = 0
    for i in range(len(a)):
        res += int(a[i]) * int(b[i])
    return res % 10
