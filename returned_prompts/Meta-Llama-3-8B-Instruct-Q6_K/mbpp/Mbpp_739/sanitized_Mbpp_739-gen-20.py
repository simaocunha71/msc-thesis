def find_Index(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    i = 1
    while True:
        tri = (i * (i + 1)) // 2
        if len(str(tri)) == n:
            return i
        i += 1