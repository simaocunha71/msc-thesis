
def multiply(a, b):
    # Convert the inputs to strings to easily access the last digit
    a = str(a)
    b = str(b)

    # Use the built-in functions to get the last digit of each number
    unit_a = int(a[-1])
    unit_b = int(b[-1])

    # Multiply the unit digits and return the result
    return unit_a * unit_b

print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14,-15)) # should return 20


# Alternatively, you can use the modulus operator to get the unit digit

def multiply(a, b):
    return (a % 10) * (b % 10)

print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14,-15)) # should return 20


# And, you can use list comprehension to do it in one line

def multiply(a, b):
    return [int(str(a)[-1]) * int(str(b)[-1])]

print(multiply(148, 412)) # should return [16]
print(multiply(19, 28)) # should return [72]
print(multiply(2020, 1851)) # should return [0]
print(multiply(14,-15)) # should return [-20]


# Finally, you can use the map function to apply the unit digit multiplication to every pair of elements in two lists

def multiply(a, b):
    return list(map(lambda x, y: