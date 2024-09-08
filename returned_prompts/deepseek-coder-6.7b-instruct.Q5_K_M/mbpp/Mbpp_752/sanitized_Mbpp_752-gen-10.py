def jacobsthal_num(n, memo={}):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        memo[n] = 2 * jacobsthal_num(n-1, memo) + jacobsthal_num(n-2, memo)
        return memo[n]