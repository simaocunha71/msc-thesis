def is_undulating(n):
    str_n = str(n)
    for i in range(len(str_n) - 1):
        if str_n[i] != str_n[i+1]:
            return False
    return True