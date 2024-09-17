
def jacobsthal_num(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 3
    if n % 2 == 0:
        return 2 * jacobsthal_num(n // 2)
    else:
        return jacobsthal_num(n + 1)


