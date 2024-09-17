def find_Index(n):
    num = 1
    while len(str(num)) < n:
        num += 1
    return len(str(num))