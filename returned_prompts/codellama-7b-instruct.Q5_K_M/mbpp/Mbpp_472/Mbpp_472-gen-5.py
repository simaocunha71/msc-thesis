def check_Consecutive(lst):
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i+1]-lst[i] != 1:
            return False
    return True



