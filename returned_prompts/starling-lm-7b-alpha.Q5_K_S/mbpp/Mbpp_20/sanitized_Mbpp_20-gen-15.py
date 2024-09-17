def is_woodall(num: int):
    num_str = str(num)
    if len(num_str) == 1:
        return True
    if int(num_str[0]) == 1:
        return False
    if int(num_str[0]) > 1:
        return False
    if num_str[1] != "0":
        return False
    for i in range(2, len(num_str)):
        if int(num_str[i]) != int(num_str[i-1]) + 1:
            return False
    return True