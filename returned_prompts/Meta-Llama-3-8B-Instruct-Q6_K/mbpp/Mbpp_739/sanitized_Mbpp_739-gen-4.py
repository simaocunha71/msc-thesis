def find_Index(n):
    count = 1
    i = 1
    while True:
        triangular = (i * (i + 1)) // 2
        if len(str(triangular)) == n:
            return count
        i += 1
        count += 1