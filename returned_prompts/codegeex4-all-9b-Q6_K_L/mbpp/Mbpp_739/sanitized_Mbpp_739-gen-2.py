def find_Index(n):
    def is_Triangular(x):
        return (1 + 8*x)**0.5 % 1 == 0

    i = 0
    while True:
        if len(str(i*(i+1)//2)) == n:
            return i
        i += 1