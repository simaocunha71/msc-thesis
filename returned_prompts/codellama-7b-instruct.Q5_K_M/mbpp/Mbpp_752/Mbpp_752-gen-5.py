
def jacobsthal_num(n):
    if n < 2:
        return 0
    else:
        return (jacobsthal_num(n-1)*n) + jacobsthal_num(n-2)


