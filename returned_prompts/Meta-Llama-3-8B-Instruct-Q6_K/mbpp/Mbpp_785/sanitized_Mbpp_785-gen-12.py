def tuple_str_int(s):
    try:
        return eval(s)
    except SyntaxError:
        raise ValueError("Invalid tuple string")