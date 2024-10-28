def bell_number(n):
    memo = {0: 1}
    for i in range(1, n+1):
        memo[i] = sum(memo.get(j, 0) for j in range(i))
    return memo[n]