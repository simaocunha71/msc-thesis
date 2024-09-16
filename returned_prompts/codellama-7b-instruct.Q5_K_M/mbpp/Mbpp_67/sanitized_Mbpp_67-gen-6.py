def bell_number(n):
    # Use the recurrence relation:
    # B(n) = sum(B(k-1)) for all k <= n
    # B(n) is the number of ways to partition a set of n items
    # into non-empty subsets.
    #
    # We're using the dynamic programming method to calculate B(n).
    # B(n) is calculated from B(k-1) for all k <= n-1.
    # So we start with B(1) = 1 and B(2) = 2.
    # Then we calculate B(3) from B(2), B(2) and B(1), and so on.
    B = [0] * (n+1)
    B[1] = 1
    B[2] = 2
    for k in range(3, n+1):
        B[k] = sum(B[k-j] for j in range(1, k))
    return B[n]