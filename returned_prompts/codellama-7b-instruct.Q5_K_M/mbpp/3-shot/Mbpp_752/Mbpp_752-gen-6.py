
def jacobsthal_num(n):
    if n <= 1:
        return 0
    return (jacobsthal_num(n - 1) + jacobsthal_num(n - 2)) * n


