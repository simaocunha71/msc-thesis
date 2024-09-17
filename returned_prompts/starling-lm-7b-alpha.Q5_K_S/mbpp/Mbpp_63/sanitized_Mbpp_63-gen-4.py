def max_difference(t):
    # t is a list of tuples
    m = -1
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            m = max(m, abs(t[i][0] - t[j][1]))
    return m
t = [(3, 5), (1, 7), (10, 3), (1, 2)]