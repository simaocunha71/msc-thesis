def is_simple_power(x, n):
    if x == 1:
        return True
    if n == 1:
        return False
    power = n
    while power < x:
        power *= n
    return power == x

print(is_simple_power(1, 4))  # => true
print(is_simple_power(2, 2))  # => true
print(is_simple_power(8, 2))  # => true
print(is_simple_power(3, 2))  # => false
print(is_simple_power(3, 1))  # => false
print(is_simple_power(5, 3))  # => false