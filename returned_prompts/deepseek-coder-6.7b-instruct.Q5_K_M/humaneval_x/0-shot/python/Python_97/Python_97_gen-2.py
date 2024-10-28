
def multiply(a, b):
    return (abs(a) % 10) * (abs(b) % 10)

print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14,-15)) # should return 20

# Or using the modulus operator:

def multiply(a, b):
    return (a % 10) * (b % 10)

print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14,-15)) # should return 20

# Or using string slicing:

def multiply(a, b):
    return int(str(a)[-1]) * int(str(b)[-1])

print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14,-15)) # should return 20

# Or using division and floor division:

def multiply(a, b):
    return ((a % 10) * (b % 10)) % 10

print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14,-15)) # should return 20
'''

# Another approach using list comprehension:

def multiply