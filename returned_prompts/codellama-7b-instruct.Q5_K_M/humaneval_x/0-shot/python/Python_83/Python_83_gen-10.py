
    ones = []
    for i in range(1, n+1):
        if str(i)[0] == '1' or str(i)[-1] == '1':
            ones.append(i)
    return len(ones)

