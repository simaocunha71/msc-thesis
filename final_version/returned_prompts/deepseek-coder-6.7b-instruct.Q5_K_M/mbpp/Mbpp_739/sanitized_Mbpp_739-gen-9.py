def find_Index(n):
    i = 1
    while True:
        t = i*(i+1)//2
        if 10**(n-1) <= t < 10**n:
            return i
        i += 1