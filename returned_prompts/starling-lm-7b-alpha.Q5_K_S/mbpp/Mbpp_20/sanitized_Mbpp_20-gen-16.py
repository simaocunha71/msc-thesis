def is_woodall(num: int):
    num_str = str(num)
    return all(c == '1' or c == '0' for c in num_str)