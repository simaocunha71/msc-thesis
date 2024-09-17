def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        jacobsthal_nums = [0, 1]
        while len(jacobsthal_nums) < n:
            jacobsthal_nums.append(jacobsthal_nums[-1] + 1)
        return jacobsthal_nums[-1]