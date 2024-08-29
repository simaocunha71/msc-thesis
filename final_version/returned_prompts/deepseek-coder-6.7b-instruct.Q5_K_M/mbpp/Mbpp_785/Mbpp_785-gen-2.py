def tuple_str_int(s):
    return eval(s)

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# or

def tuple_str_int(s):
    return tuple(map(int, s.strip("()").split(",")))

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# or

def tuple_str_int(s):
    return eval(s)

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# or

def tuple_str_int(s):
    return tuple(int(i) for i in s[1:-1].split(','))

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# or

def tuple_str_int(s):
    return eval(s)

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# or

def tuple_str_int(s):
    return tuple(map(int, s.replace('(', '').replace(')', '').split(',')))

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# or

def tuple_str_int(s):
    return tuple(map(int, s[1:-1].split(',')))

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# or

def tuple_str_int(s):
    return tuple(map(int, s.replace("(", "").replace(")", "").split(",")))

assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)

# or

def tuple_str_int(s):
    return tuple(int(i) for i in s.