
def is_woodall(num):
    num_str = str(num)
    if num_str.count("0") > 0:
        return False
    else:
        if num_str.count("1") == 1:
            return True
        else:
            return False


