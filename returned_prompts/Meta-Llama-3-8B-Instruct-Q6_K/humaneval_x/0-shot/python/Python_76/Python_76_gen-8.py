def is_simple_power(x, n):
    import math
    root = math.pow(n, 1.0 / int(math.log(x, n)))
    return round(root) ** int(math.log(x, n)) == x
print(is_simple_power(1, 4)) #True
print(is_simple_power(2, 2)) #True
print(is_simple_power(8, 2)) #True
print(is_simple_power(3, 2)) #False
print(is_simple_power(3, 1)) #False
print(is_simple_power(5, 3)) #False
print(is_simple_power(9, 3)) #True
print(is_simple_power(16, 4)) #True
print(is_simple_power(25, 5)) #True
print(is_simple_power(27, 3)) #True
print(is_simple_power(100, 10)) #True
print(is_simple_power(1024, 4)) #True
print(is_simple_power(125, 5)) #True
print(is_simple_power(144, 12)) #True
print(is_simple_power(81, 4)) #True
print(is_simple_power(36, 6)) #True
print(is_simple_power(729, 9)) #True
print(is_simple_power(64, 8)) #True
print(is_simple_power(256, 16)) #True
print(is_simple_power(9, 1)) #False
print(is_simple_power(0, 1)) #False
print(is_simple_power(0, 0)) #False
print(is_simple_power(1, 0)) #False
print(is_simple_power(0, 2)) #False
print(is_simple_power(1, 0)) #False
print(is_simple_power(0, 1)) #False
print(is_simple_power(1, 2)) #False
print(is_simple_power(1, 3)) #False
print(is_simple_power(1, 4)) #True
print(is_simple_power(1, 5)) #False
print(is_simple_power(1, 6)) #False
print(is_simple_power(1, 7)) #False
print(is_simple_power(1, 8)) #False
print(is_simple_power(1, 9)) #False
print(is_simple_power(1, 10)) #False
print(is_simple_power(1, 11