def is_undulating(n):
    str_n = str(n)
    for i in range(1, len(str_n)):
        if str_n[i] == str_n[i-1]:
            return False
    return True

