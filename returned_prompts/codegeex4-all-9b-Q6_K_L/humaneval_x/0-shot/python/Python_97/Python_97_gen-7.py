def multiply(a, b):
    return abs(a%10) * abs(b%10)

print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14,-15)) # should return 20