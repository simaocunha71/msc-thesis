def find_Index(n):
    num = 1
    i = 1
    while True:
        if len(str(num)) == n:
            return i
        num += i
        i += 1