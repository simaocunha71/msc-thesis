def is_woodall(num):
    num_str = str(num)
    num_len = len(num_str)
    if num_str == '1':
        return True
    elif num_str[0] == '2' or num_str[0] == '3' or num_str[0] == '4' or num_str[0] == '5' or num_str[0] == '6' or num_str[0] == '7' or num_str[0] == '8' or num_str[0] == '9':
        return False
    else:
        num_str = num_str[1:]
        num_len -= 1
        if len(num_str) != num_len:
            return False
        else:
            return True