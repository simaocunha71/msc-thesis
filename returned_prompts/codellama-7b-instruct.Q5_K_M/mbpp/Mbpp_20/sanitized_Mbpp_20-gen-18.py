def is_woodall(num):
    num_str = str(num)
    if len(num_str) != 3:
        return False
    for i in range(len(num_str)):
        if int(num_str[i]) != int(num_str[0]) + i:
            return False
    return True