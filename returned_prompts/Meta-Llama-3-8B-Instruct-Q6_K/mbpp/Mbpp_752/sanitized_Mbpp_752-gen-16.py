def jacobsthal_num(n):
    if n <= 1:
        return n
    jacobsthal = [0, 1]
    while len(jacobsthal) < n:
        jacobsthal.append(jacobsthal[-1] + jacobsthal[-2] * 2)
    return jacobsthal[-1]