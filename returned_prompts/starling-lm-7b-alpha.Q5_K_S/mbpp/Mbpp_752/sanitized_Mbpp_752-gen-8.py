def jacobsthal_num(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 1
    elif n==3:
        return 3
    else:
        a, b, c = 1, 1, 3
        for _ in range(n-3):
            a, b, c = c, b+c, a+b+c
        return a+b+c