    if n % 2 != 0:
        return False

    for i in range(2, n, 2):
        for j in range(i+2, n, 2):
            for k in range(j+2, n, 2):
                for l in range(k+2, n, 2):
                    if i + j + k + l == n:
                        return True

    return False

