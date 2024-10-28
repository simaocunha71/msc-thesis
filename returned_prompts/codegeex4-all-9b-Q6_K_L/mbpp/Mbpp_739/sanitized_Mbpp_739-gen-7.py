def find_Index(n):
    def is_Triangular(num):
        i = 1
        while num > 0:
            num -= i
            i += 1
        return num == 0

    i = 0
    num = 0
    while True:
        num += i
        if len(str(num)) == n and is_Triangular(num):
            return i
        i += 1