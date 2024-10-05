    for i in range(2, n // 4 + 1):
        for j in range(i + 2, n // 2 + 1, 2):
            for k in range(j + 2, n - i - j + 1, 2):
                if i + j + k + (n - i - j - k) == n:
                    return True
    return False


