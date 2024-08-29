def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

assert check_integer("python") == False
assert check_integer("123") == True
assert check_integer("-456") == True
assert check_integer("0") == True

