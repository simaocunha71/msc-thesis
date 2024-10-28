def tuple_str_int(s):
    # remove the parentheses and split the string by comma
    l = s.strip('()').split(',')
    # convert each element to integer and return as a tuple
    return tuple(map(int, l))