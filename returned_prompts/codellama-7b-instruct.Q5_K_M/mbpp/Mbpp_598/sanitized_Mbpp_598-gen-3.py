def armstrong_number(n):
    return n == sum(map(lambda x: x**3, str(n)))