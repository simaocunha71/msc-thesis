def is_polite(n):
    i = 1
    polite_nums = []
    while len(polite_nums) < n:
        i += 1
        for j in range(1, i):
            if i - j - j in polite_nums:
                polite_nums.append(i - j - j)
    return polite_nums[-1] + 1