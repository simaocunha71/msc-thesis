def find_Index(n):
    i = 1
    while True:
        if len(str(i*(i+1)//2)) == n:
            return i
        i += 1