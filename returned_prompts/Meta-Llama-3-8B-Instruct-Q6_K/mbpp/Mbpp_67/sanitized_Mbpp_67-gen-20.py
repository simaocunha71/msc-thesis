def bell_number(n):
    if n == 0:
        return 1
    else:
        return sum([bell_number(k) * bell_number(n-1-k) for k in range(n+1)])