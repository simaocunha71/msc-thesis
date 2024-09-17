def bell_Number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        B = [1, 1]
        for i in range(2, n):
            B.append(B[i-1] + sum(B[:i]))
        return B[-1]