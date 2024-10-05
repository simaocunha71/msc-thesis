def is_simple_power(x, n):
    if x == 0 or n == 0:
        return False
    if x < 0 or n < 0:
        return False
    if x == 1 or n == 1:
        return True
    if x == n:
        return True
    if x % n != 0:
        return False
    while x % n == 0:
        x = x / n
    if x == 1:
        return True
    else:
        return False

print(is_simple_power(1, 4)) # true
print(is_simple_power(2, 2)) # true
print(is_simple_power(8, 2)) # true
print(is_simple_power(3, 2)) # false
print(is_simple_power(3, 1)) # false
print(is_simple_power(5, 3)) # false
print(is_simple_power(2, 3)) # false
print(is_simple_power(1, 0)) # false
print(is_simple_power(0, 3)) # false
print(is_simple_power(0, 0)) # false
print(is_simple_power(-1, 3)) # false
print(is_simple_power(1, -3)) # false
print(is_simple_power(-1, -3)) # false
print(is_simple_power(2, -3)) # false
print(is_simple_power(-2, -3)) # false
print(is_simple_power(-2, 3)) # false
print(is_simple_power(3, -2)) # false
print(is_simple_power(-3, -2)) # false
print(is_simple_power(-3, 2)) # false
print(is_simple_power(4, 2)) # true
print(is_simple_power(8, 2)) # true
print(is_simple_power(16, 2)) # true
print(is_simple_power(32, 2)) # true
print(is_simple_power(64, 2)) # true
print(is_simple_power(128, 2)) # true
print(is_simple_power(256, 2)) # true
print(is_simple_power(512, 2)) # true
print(is_simple_power(1024, 2)) # true
print(is_simple_power(2048, 2)) # true
print(is_simple_power(4096, 2)) # true
print(is_simple_power(