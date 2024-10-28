def jacobsthal_num(n):
    if n == 1 or n == 2:
        return 0
    elif n == 3:
        return 1
    else:
        jacobsthal = [0, 0, 1]
        for i in range(3, n):
            jacobsthal.append(jacobsthal[i-1] + 2*jacobsthal[i-2])
        return jacobsthal[n-1]  # return the nth jacobsthal number