def tuple_str_int(s):
    return eval(s)  # This is not recommended for untrusted input. It's better to use ast.literal_eval() for trusted input. For untrusted input, you should parse the string manually or use a safe evaluation function.
    # return tuple(map(int, s.strip('()').split(',')))  # safer option for untrusted input
    # return tuple(map(int, s[1:-1].split(',')))  # safer option for untrusted input