def jacobsthal_num(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        prev = 0
        curr = 1
        for _ in range(2, n):
            prev, curr = curr, prev + curr
        return curr