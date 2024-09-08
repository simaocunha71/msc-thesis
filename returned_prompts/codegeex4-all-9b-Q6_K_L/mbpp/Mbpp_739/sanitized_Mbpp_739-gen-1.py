def find_Index(n):
    i = 1
    T = 1
    while len(str(T)) != n:
        i += 1
        T = T + i
    return i