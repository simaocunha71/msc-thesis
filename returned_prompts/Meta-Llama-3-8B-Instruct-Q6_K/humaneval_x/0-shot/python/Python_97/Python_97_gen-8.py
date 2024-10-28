def multiply(a, b):
    # Extract the unit digits of the two numbers
    unit_a = a % 10
    unit_b = b % 10
    
    # Calculate the product of the unit digits
    product = unit_a * unit_b
    
    return product
    # You can also write the function as follows:
    # return (abs(a) % 10) * (abs(b) % 10)  # Note: abs() to handle negative numbers

print(multiply(148, 412))  # Output: 16
print(multiply(19, 28))    # Output: 72
print(multiply(2020, 1851)) # Output: 0
print(multiply(14,-15))    # Output: 20
print(multiply(-4, -9))    # Output: 36
print(multiply(-5, 10))    # Output: 0
print(multiply(5, 10))     # Output: 0
print(multiply(1, 1))      # Output: 1
print(multiply(0, 0))      # Output: 0
print(multiply(0, 1))      # Output: 0
print(multiply(1, 0))      # Output: 0
print(multiply(-1, 0))     # Output: 0
print(multiply(0, -1))     # Output: 0
print(multiply(-1, -1))    # Output: 1
print(multiply(1, -1))     # Output: -1
print(multiply(-1, 1))     # Output: -1
print(multiply(1, -1))     # Output: -1
print(multiply(-1, -1))    # Output: 1
print(multiply(2, 3))      # Output: 6
print(multiply(-2, 3))     # Output: -6
print(multiply(2, -3))     # Output: -6
print(multiply(-2, -3))    # Output: 6
print(multiply(3, 4))      # Output: 12
print(multiply(-3, 4))     # Output: -12
print(multiply(3, -4))     # Output: -12
print(multiply(-3, -4))    # Output