def find_Index(n):
    i = 1
    while len(str(i*(i+1)//2)) < n:
        i += 1
    return i