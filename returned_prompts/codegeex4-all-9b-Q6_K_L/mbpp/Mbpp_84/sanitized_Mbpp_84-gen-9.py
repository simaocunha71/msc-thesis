def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        s = [1, 2]
        for i in range(2, n):
            s.append(s[s[-2] - 1] + s[s[-1] - 1])
        return s[-1]