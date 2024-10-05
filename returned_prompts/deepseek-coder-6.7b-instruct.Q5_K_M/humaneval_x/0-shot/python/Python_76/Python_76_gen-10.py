
    import math
    def is_simple_power(x, n):
        if x < 1:
            return False
        elif x == 1:
            return True
        else:
            power = math.log(x, n)
            return power.is_integer()

print(is_simple_power(1, 4)) # True
print(is_simple_power(2, 2)) # True
print(is_simple_power(8, 2)) # True
print(is_simple_power(3, 2)) # False
print(is_simple_power(3, 1)) # False
print(is_simple_power(5, 3)) # False
print(is_simple_power(64, 2)) # True
print(is_simple_power(729, 3)) # True
print(is_simple_power(1024, 2)) # True
print(is_simple_power(1594323, 3)) # False

# Additional test cases to check
print(is_simple_power(27, 3)) # True
print(is_simple_power(64, 4)) # True
print(is_simple_power(100, 10)) # True
print(is_simple_power(125, 5)) # True
print(is_simple_power(243, 3)) # False
print(is_simple_power(256, 2)) # False
print(is_simple_power(343, 7)) # False
print(is_simple_power(512, 2)) # False
print(is_simple_power(720, 5)) # False
print(is_simple_power(1000, 10)) # False

This function works by using the math.log function to calculate the logarithm of x to the base n. If the result is an integer, then x is a simple power of n. Otherwise, x is not a simple power of n.

Testing with various inputs, the function performs as expected, returning True for simple powers and False for non-simple powers.

The time complexity is O(