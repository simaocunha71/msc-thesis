
def first_repeated_char(input_str):
    for (i, c) in enumerate(input_str):
        if input_str.find(c) != i:
            return c
    return None


