    for i in range(2, n + 1, 2):
        for j in range(i, n + 1, 2):
            for k in range(j, n + 1, 2):
                for m in range(k, n + 1, 2):
                    if i + j + k + m == n:
                        return True
    return False
