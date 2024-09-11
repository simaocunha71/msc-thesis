def is_Diff(n):
    n = str(n)
    for i in range(len(n)):
        if int(n[i]) - int(n[i-1]) != 0:
            return False
    return True