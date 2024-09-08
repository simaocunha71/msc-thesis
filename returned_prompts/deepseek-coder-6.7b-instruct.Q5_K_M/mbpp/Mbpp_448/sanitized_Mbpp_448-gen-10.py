def cal_sum(n):
    P0, P1, P2 = 3, 0, 2
    if n == 0:
        return P0
    elif n == 1:
        return P1
    elif n == 2:
        return P2
    else:
        for i in range(3, n+1):
            Pn = P0 + P1 + P2
            P0, P1, P2 = P1, P2, Pn
        return Pn