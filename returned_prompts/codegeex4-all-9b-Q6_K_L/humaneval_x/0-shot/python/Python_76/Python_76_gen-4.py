def is_simple_power(x, n):
    return x ** (1.0 / n) == int(x ** (1.0 / n))

print(is_simple_power(1, 4)) # => true
print(is_simple_power(2, 2)) # => true
print(is_simple_power(8, 2)) # => true
print(is_simple_power(3, 2)) # => false
print(is_simple_power(3, 1)) # => false
print(is_simple_power(5, 3)) # => false