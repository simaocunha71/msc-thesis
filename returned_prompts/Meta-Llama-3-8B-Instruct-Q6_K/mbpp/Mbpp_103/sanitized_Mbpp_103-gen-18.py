def eulerian_num(n, m):
    if m < 0 or m > n:
        return 0
    result = 0
    for k in range(m+1):
        result += (-1)**(n-k-1) * math.factorial(n-1) // (math.factorial(k) * math.factorial(n-k-1))
    return result