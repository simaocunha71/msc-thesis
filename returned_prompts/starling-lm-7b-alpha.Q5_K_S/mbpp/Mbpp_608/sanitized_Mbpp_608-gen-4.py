def bell_Number(n):
    bells = [0, 1]
    for i in range(2, n + 1):
        bells.append(sum(bells[i - 1::]))
    return bells[n]