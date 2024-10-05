    for i in range(2, n, 2):
        if i * 4 == n:
            return True
        for j in range(2, (n - i) // 2, 2):
            if i + j * 2 == n:
                return True
            for k in range(2, (n - i - j * 2) // 2, 2):
                if i + j * 2 + k * 4 == n:
                    return True
                for last in range(2, (n - i - j * 2 - k * 4) // 2, 2):
                    if i + j * 2 + k * 4 + last * 2 == n:
                        return True
    return False


