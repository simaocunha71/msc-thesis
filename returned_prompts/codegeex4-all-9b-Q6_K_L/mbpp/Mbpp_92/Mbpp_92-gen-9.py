def is_undulating(n):
    str_n = str(n)
    return all(str_n[i] != str_n[i+1] for i in range(len(str_n)-1))

