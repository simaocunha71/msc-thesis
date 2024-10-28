def get_max_sum(n):
    if n < 1:
        return 0
    if n <= 60:
        return [0, n, n, n, n, n][n]
    divs = get_divisors(n)
    max_sums = []
    for d in divs:
        max_sums.append(get_max_sum(d))
    max_sums.sort(reverse=True)
    return max_sums[0] + n