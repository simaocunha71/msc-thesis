def check_Consecutive(lst):
    return len(lst) > 1 and all(lst[i] + 1 == lst[i+1] for i in range(len(lst)-1))