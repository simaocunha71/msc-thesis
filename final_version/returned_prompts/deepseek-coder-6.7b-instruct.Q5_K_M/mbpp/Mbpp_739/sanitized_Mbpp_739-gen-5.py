def find_Index(n):
    i = 1
    while True:
        num = i*(i+1)//2
        if len(str(num)) == n:
            return i
        i += 1