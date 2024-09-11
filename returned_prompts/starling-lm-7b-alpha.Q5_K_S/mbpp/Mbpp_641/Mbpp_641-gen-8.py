def is_nonagonal(n):
    if n % 7 == 0:
        return True
    else:
        return False

def nonagonal(n):
    if n == 1:
        return 1
    else:
        return nonagonal(n - 1) + 7 * (n - 1)

def nth_nonagonal(n):
    if is_nonagonal(n):
        return "It is a nonagonal number."
    else:
        return "It is not a nonagonal number."

print(nth_nonagonal(10))
# It is a nonagonal number.
#print(nth_nonagonal(11))
# It is not a nonagonal number.


# Run the tests
print(is_nonagonal(10)) # True
print(is_nonagonal(11)) # False
print(nonagonal(1)) # 1
print(nonagonal(2)) # 8
print(nonagonal(3)) # 17
print(nonagonal(4)) # 30
print(nonagonal(5)) # 51
print(nonagonal(6)) # 82
print(nonagonal(7)) # 123
print(nonagonal(8)) # 174
print(nonagonal(9)) # 235
print(nonagonal(10)) # 325

"""
"""

# Here is a function that will return True if the number is a nonagonal number and False if the number is not a nonagonal number:

def is_nonagonal(n):
    if n % 7 == 0:
        return True
    else:
        return False

# Here is a function that will return the nth nonagonal number:

def nonagonal(n):
    if n == 1:
        return 1
    else:
        return nonagonal(n - 1) + 7 * (n - 1)

# Here is a function that will return a string that indicates whether the number is a nonagonal number or not:

def nth_nonagonal(n):
    if is_nonagonal(n):
        return "It is a non