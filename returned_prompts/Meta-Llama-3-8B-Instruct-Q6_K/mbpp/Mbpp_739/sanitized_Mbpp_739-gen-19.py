def find_Index(n):
    i = 1
    while True:
        triangular_num = (i * (i + 1)) // 2
        if len(str(triangular_num)) == n:
            return i + 1
        i += 1