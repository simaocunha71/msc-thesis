def check_Consecutive(lst):
    if len(lst) < 2:
        return False
    return all(lst[i] + 1 == lst[i + 1] for i in range(len(lst) - 1))