def frequency(a, b):
    count = 0
    for elem in a:
        if elem == b:
            count += 1
    return count