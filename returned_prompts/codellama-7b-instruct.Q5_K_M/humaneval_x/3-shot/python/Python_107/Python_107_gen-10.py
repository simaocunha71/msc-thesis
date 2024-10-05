    count_even, count_odd = 0, 0
    for i in range(1, n + 1):
        s = str(i)
        if s == s[::-1]:
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return count_even, count_odd


