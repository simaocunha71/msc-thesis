    if n == 0 or n == 1:
        return 0

    elif n == 2:
        return 1

    else:
        fibs = [0, 0, 1]
        while len(fibs) < n + 1:
            fibs.append(fibs[-1] + fibs[-2] + fibs[-3])

        return fibs[-1]


