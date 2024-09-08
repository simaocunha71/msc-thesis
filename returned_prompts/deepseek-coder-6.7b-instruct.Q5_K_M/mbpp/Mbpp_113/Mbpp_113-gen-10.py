def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print(check_integer("python")) # False
print(check_integer("123")) # True
print(check_integer("-123")) # True
print(check_integer("0")) # True

