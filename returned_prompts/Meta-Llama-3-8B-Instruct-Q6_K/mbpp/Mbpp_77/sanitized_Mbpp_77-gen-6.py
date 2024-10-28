def is_Diff(n):
    if sum(int(i) for i in str(n)) % 11 == 0:
        return True
    else:
        return False