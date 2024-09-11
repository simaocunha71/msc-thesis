def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = [0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731]
        return a[n-1]+2*a[n-2]+a[n-3]