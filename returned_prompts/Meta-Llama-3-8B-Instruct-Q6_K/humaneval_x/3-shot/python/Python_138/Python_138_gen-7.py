    for i in range(2, n):
        if i % 2 == 0:
            for j in range(2, (n - i) // 2):
                if j % 2 == 0:
                    for k in range(2, (n - i - j) // 2):
                        if k % 2 == 0:
                            for m in range(2, (n - i - j - k) // 2):
                                if m % 2 == 0:
 if i + j + k + m == n:
 return True
    return False


