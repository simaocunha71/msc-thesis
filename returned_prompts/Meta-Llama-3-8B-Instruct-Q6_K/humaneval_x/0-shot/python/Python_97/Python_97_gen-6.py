def multiply(a, b):
    unit_digit_a = a % 10
    unit_digit_b = b % 10
    product = unit_digit_a * unit_digit_b
    return product
# test cases
print(multiply(148, 412)) # should return 16
print(multiply(19, 28)) # should return 72
print(multiply(2020, 1851)) # should return 0
print(multiply(14, -15)) # should return 20
print(multiply(11, 22)) # should return 4
print(multiply(13, 31)) # should return 4
print(multiply(17, 37)) # should return 1
print(multiply(19, 39)) # should return 1
print(multiply(10, 20)) # should return 0
print(multiply(20, 30)) # should return 0
print(multiply(-2, -3)) # should return 6
print(multiply(2, -3)) # should return -6
print(multiply(-2, 3)) # should return -6
print(multiply(2, 3)) # should return 6
print(multiply(0, 0)) # should return 0
print(multiply(-2, 0)) # should return 0
print(multiply(0, -2)) # should return 0
print(multiply(2, 0)) # should return 0
print(multiply(0, 2)) # should return 0
print(multiply(-2, -2)) # should return 4
print(multiply(2, 2)) # should return 4
print(multiply(-2, 2)) # should return -4
print(multiply(2, -2)) # should return -4
print(multiply(-2, 2)) # should return -4
print(multiply(2, -2)) # should return -4
print(multiply(0, 0)) # should return 0
print(multiply(-2, -2)) # should return 4
print(multiply(2, 2)) # should return 4
print(multiply(-2, 2)) # should return -4
print(multiply(2, -2)) # should return -4
print(multiply(-2, -2)) # should return 4
