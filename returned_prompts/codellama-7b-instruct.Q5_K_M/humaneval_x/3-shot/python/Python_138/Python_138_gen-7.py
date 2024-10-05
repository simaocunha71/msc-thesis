    for i in range(1, n//2 + 1):
        for j in range(1, n//2 + 1):
            for k in range(1, n//2 + 1):
                for l in range(1, n//2 + 1):
                    if i + j + k + l == n:
                        if i % 2 == 0 and j % 2 == 0 and k % 2 == 0 and l % 2 == 0:
                            return True

    return False


