
def is_simple_power(x, n):
    if n == 1 and x != 1:
        return True
    elif n == 1 and x == 1:
        return False
    elif x == 0:
        return True
    elif x < 0 or n < 0:
        return False
    else:
        while x % n == 0:
            x /= n
        return x == 1

# test cases
print(is_simple_power(1, 4)) # => true
print(is_simple_power(2, 2)) # => true
print(is_simple_power(8, 2)) # => true
print(is_simple_power(3, 2)) # => false
print(is_simple_power(3, 1)) # => false
print(is_simple_power(5, 3)) # => false
print(is_simple_power(64, 2)) # => true
print(is_simple_power(729, 3)) # => true
print(is_simple_power(1024, 2)) # => true
print(is_simple_power(15625, 5)) # => true

Note: This problem can be solved using logarithms if we are allowed to use math library.
"""

import math
def is_simple_power(x, n):
    if x <= 0 or n <= 0:
        return False
    else:
        return math.isclose(math.log(x, n), round(math.log(x, n)))

# test cases
print(is_simple_power(1, 4)) # => true
print(is_simple_power(2, 2)) # => true
print(is_simple_power(8, 2)) # => true
print(is_simple_power(3, 2)) # => false
print(is_simple_power(3, 1)) # => false
print(is_simple_power(5, 3)) # => false
print(is_simple_power(64, 2)) # => true
print(is_simple_power(729, 3)) # => true
print(is_