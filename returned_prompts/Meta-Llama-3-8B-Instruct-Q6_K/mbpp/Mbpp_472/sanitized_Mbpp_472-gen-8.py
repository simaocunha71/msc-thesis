def check_Consecutive(lst):
    for i in range(len(lst) - 1):
        if abs(lst[i] - lst[i+1]) != 1:
            return False
    return True