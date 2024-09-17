
def is_undulating(num: int) -> bool:
    num_str = str(num)
    if len(num_str) == 1:
        return False
    for i in range(1, len(num_str)):
        if abs(int(num_str[i]) - int(num_str[i-1])) != 1:
            return False
    return True


