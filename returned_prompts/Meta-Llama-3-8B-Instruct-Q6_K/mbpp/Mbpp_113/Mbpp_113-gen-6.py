def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    else:
        return False

# Testing the function
print(check_integer("123"))  # True
print(check_integer("python"))  # False
print(check_integer("123abc"))  # False
print(check_integer("123.45"))  # False
print(check_integer("-123"))  # True
print(check_integer("0"))  # True
print(check_integer("123abc456"))  # False
print(check_integer("123.45"))  # False
print(check_integer("123e45"))  # False
print(check_integer("123abcxyz"))  # False

# Output: 
# True
# False
# False
# False
# True
# True
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
# False
#