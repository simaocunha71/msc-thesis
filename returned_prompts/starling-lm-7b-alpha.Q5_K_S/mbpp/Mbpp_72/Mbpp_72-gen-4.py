def dif_Square(n):
    for i in range(int(n**0.5), -1, -1):
        if n % i == 0:
            return True
    return False


# Another approach is to use the square root of the number.
from math import sqrt
def dif_Square_1(n):
    return (int(sqrt(n)) + 1) ** 2 - n == 0


assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(16) == True

# Using the built-in pow() function.
def dif_Square_2(n):
    return (pow(int(sqrt(n)) + 1, 2) - n) == 0


assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(16) == True

# Using the built-in pow() function with the second parameter set to 2.
def dif_Square_3(n):
    return pow(int(sqrt(n)) + 1, 2) - n == 0


assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(16) == True

# Using the built-in pow() function with the second parameter set to 4.
def dif_Square_4(n):
    return pow(int(sqrt(n)), 4) - n == 0


assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(16) == True

# Using the built-in pow() function with the second parameter set to 2 and the third parameter set to 2.
def dif_Square_5(n):
    return pow(int(sqrt(n)), 2, 2) - n == 0


assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(16) == True

# Using the built-in pow() function with