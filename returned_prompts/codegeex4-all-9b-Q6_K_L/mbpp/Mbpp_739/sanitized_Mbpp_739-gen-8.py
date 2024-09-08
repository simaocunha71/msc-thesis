def find_Index(n):
    def is_triangular(k):
        i = 1
        while True:
            if k == (i * (i + 1)) // 2:
                return True
            if k < (i * (i + 1)) // 2:
                return False
            i += 1

    i = 0
    while True:
        if is_triangular(i) and len(str(i)) == n:
            return i
        i += 1