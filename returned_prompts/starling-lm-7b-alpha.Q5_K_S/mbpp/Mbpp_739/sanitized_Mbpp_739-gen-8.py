def find_Index(n):
    count = 0
    for i in range(1, 10 ** n):
        if i * (i + 1) // 2 < 10 ** n:
            count += 1
        else:
            break
    return count