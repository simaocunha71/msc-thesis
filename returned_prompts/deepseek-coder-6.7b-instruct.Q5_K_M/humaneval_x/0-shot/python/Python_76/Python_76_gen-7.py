
    import math

    def is_simple_power(x, n):
        if x == 1:
            return True
        if n <= 1 or x <= 0:
            return False
        power = math.log(x, n)
        return power.is_integer()

print(is_simple_power(1, 4)) # True
print(is_simple_power(2, 2)) # True
print(is_simple_power(8, 2)) # True
print(is_simple_power(3, 2)) # False
print(is_simple_power(3, 1)) # False
print(is_simple_power(5, 3)) # False
print(is_simple_power(64, 4)) # True
print(is_simple_power(16, 2)) # True
print(is_simple_power(27, 3)) # True
print(is_simple_power(18, 3)) # False
print(is_simple_power(36, 6)) # True
print(is_simple_power(35, 5)) # False
print(is_simple_power(729, 9)) # True
print(is_simple_power(81, 3)) # True
print(is_simple_power(1024, 4)) # True
print(is_simple_power(121, 3)) # True
print(is_simple_power(144, 4)) # True
print(is_simple_power(216, 6)) # True
print(is_simple_power(243, 9)) # True
print(is_simple_power(270, 6)) # False
print(is_simple_power(324, 6)) # False
print(is_simple_power(361, 7)) # False
print(is_simple_power(400, 5)) # False
print(is_simple_power(432, 6)) # True
print(is_simple_power(486, 6)) # False
print(is_simple_power(512, 