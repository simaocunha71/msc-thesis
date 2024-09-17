def check_Consecutive(lst):
    for i in range(len(lst)-1):
        if abs(lst[i+1]-lst[i]) > 1:
            return False
    return True