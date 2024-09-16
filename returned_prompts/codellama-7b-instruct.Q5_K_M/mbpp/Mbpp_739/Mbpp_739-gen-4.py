def find_Index(n):
    num = 1
    while len(str(num)) < n:
        num += 1
    for i in range(num, num*2):
        if len(str(i)) == n and i % 2 == 0 and i % 3 == 0 and i % 5 == 0:
            return i
    return -1
