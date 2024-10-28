
    def is_simple_power(x, n):
        if n == 1:
            return x == 1
        else:
            i = 1
            while i <= x:
                if n ** i == x:
                    return True
                i += 1
            return False

# Test cases
print(is_simple_power(1, 4))  # => true
print(is_simple_power(2, 2))  # => true
print(is_simple_power(8, 2))  # => true
print(is_simple_power(3, 2))  # => false
print(is_simple_power(3, 1))  # => false
print(is_simple_power(5, 3))  # => false

# Test cases 2
print(is_simple_power(27, 3))  # => true
print(is_simple_power(64, 4))  # => true
print(is_simple_power(16, 2))  # => true
print(is_simple_power(5, 2))  # => false
print(is_simple_power(25, 5))  # => true
print(is_simple_power(81, 3))  # => true
print(is_simple_power(121, 11))  # => true
print(is_simple_power(243, 3))  # => true
print(is_simple_power(49, 7))  # => false
print(is_simple_power(1024, 2))  # => true
print(is_simple_power(1, 1))  # => true
print(is_simple_power(25, 5))  # => true
print(is_simple_power(81, 3))  # => true
print(is_simple_power(121, 11))  # => true
print(is_simple_power(243, 3))  # => true
print(is_simple_power(49, 7))  # => false
print(is_simple_power(1024, 2)) 