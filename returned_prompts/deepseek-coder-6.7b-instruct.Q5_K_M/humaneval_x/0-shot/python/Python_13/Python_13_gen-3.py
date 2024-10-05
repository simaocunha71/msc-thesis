

def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

print(greatest_common_divisor(3, 5))
print(greatest_common_divisor(25, 15))

# Output:
# 1
# 5


Explanation:

In the function, we use Euclidean algorithm to find the greatest common divisor. The algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.
'''

# Task 3

'''
