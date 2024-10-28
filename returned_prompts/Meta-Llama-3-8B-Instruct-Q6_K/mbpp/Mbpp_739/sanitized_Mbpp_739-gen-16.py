def find_Index(n):
    def triangular_number(k):
        return k*(k+1)//2

    i = 1
    while True:
        if len(str(triangular_number(i))) == n:
            return i
        i += 1