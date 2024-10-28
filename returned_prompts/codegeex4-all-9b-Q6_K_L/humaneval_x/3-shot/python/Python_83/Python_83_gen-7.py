    count = 0
    for i in range(1, 10):
        if i == 1:
            count += 10 ** (n - 1)
        else:
            count += 10 ** (n - 1) - 10 ** (n - 2)
    return count

