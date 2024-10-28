def is_woodall(n):
    num_str = str(n)
    if len(num_str) != 3:
        return False
    if num_str[0] != num_str[2]:
        return False
    if num_str[1] != num_str[1]:
        return False
    return True