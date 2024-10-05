
def multiply(a, b):
    a = abs(a)
    b = abs(b)
    while a > 9:
        a = a // 10
    while b > 9:
        b = b // 10
    return a * b

print(multiply(148, 412))  # should return 16
print(multiply(19, 28))  # should return 72
print(multiply(2020, 1851))  # should return 0
print(multiply(14,-15))  # should return 20


