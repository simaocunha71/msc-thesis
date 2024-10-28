def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False
    # if s.isdigit():
    #     return True
    # else:
    #     return False
assert check_integer("123") == True
assert check_integer("python") == False
assert check_integer("123a") == False
assert check_integer("123.12") == False
assert check_integer("") == False
assert check_integer("0") == True
assert check_integer("12345678901234567890") == True
assert check_integer("-123") == True
assert check_integer("-12345678901234567890") == True
assert check_integer("123456789012345678901234567890") == True
assert check_integer("123abc") == False
assert check_integer("123.abc") == False
assert check_integer("123abc.123") == False
assert check_integer("123.123abc") == False
assert check_integer("123abc123") == True
assert check_integer("123.123") == True
assert check_integer("123.123.123") == True
assert check_integer("-123.123") == True
assert check_integer("-123.123.123") == True
assert check_integer("123abc123.123.123") == False
assert check_integer("123.123.123abc") == False
assert check_integer("123abc.123.123abc") == False
assert check_integer("123.123.123.123") == True
assert check_integer("123.123.123.123abc") == False
assert check_integer("123.123.123.123.123") == True
assert check_integer("123.123.123.123.123abc") == False
assert check_integer("123.123.123.123.123.123") == True
assert check_integer("123.123.123.123.123.123abc") == False
assert check_integer("123.123.123.123.123.123.123") == True
assert check_integer("123.123.123.123.123.123.123abc") == False
assert check_integer("123.123.123.123.123.123.123.123") == True
assert check_integer("123.123.123.123.123.123.123.123abc") == False
assert check_integer("123.123.123.123