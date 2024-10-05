    for i in range(2, n):
        if i % 2 == 0:
            for j in range(i, n):
                if j % 2 == 0:
                    for k in range(j, n):
                        if k % 2 == 0:
                            for m in range(k, n):
                                if m % 2 == 0:
 if i + j + k + m == n:
 return True
    return False


