def check_Consecutive(lst):
    if len(lst) < 2:
        return False
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] != 1:
            return False
    return True