def is_simple_power(x, n):
    if x == 1:
        return True
    if x == n:
        return True
    for i in range(2, 100):
        if n**i == x:
            return True
    return False

print(is_simple_power(1, 4))
print(is_simple_power(2, 2))
print(is_simple_power(8, 2))
print(is_simple_power(3, 2))
print(is_simple_power(3, 1))
print(is_simple_power(5, 3))