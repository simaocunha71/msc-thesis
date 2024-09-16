def find_Index(n):
    index = 1
    while len(str(index * (index + 1) // 2)) != n:
        index += 1
    return index