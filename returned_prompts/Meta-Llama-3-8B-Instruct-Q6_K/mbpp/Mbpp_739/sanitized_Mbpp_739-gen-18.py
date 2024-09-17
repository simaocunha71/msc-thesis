def find_Index(n):
    i = 1
    count = 0
    while True:
        triangular_number = i * (i + 1) // 2
        count += len(str(triangular_number))
        if count == n:
            return i
        i += 1