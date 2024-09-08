def is_woodall(n):
    i = 1
    while 2*i <= n:
        j = i + 1
        while j <= n:
            if j*(j+1) == 2*n:
                return True
            if j*(j+1) > 2*n:
                break
            j += 1
        i += 1
    return False