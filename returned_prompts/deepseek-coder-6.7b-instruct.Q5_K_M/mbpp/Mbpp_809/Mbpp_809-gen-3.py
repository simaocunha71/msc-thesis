def check_smaller(t1, t2):
    for i in range(len(t1)):
        if t1[i] >= t2[i]:
            return False
    return True

assert check_smaller((1, 2, 3), (2, 3, 4)) == False
assert check_smaller((1, 2, 3), (0, 2, 3)) == True
assert check_smaller((1, 2, 3), (1, 2, 3)) == False
assert check_smaller((1, 2, 3), (2, 1, 3)) == False
assert check_smaller((1, 2, 3), (3, 2, 1)) == False
assert check_smaller((1, 2, 3, 4), (2, 3, 4)) == False
assert check_smaller((1, 2, 3, 4), (1, 2, 3, 4)) == False
assert check_smaller((1, 2, 3, 4), (2, 2, 3, 4)) == True
assert check_smaller((1, 2, 3, 4), (2, 3, 3, 4)) == True
assert check_smaller((1, 2, 3, 4), (2, 3, 4, 4)) == True
assert check_smaller((1, 2, 3, 4), (2, 3, 4, 5)) == True
"""

Test the function with some test cases
"""
print(check_smaller((1, 2, 3), (2, 3, 4)))  # False
print(check_smaller((1, 2, 3), (0, 2, 3)))  # True
print(check_smaller((1, 2, 3), (1, 2, 3)))  # False
print(check_smaller((1, 2, 3), (2, 1, 3)))  # False
print(check_smaller((1, 2, 3), (3, 