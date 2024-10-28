    return n * (n - 1)
    # The reason is that for each car, there is exactly one other car that can collide with it. So the number of collisions is n choose 2, which is n*(n-1) for large n. But since the cars don't stop after a collision, the same collision can be counted multiple times, so we divide by 2. However, for large n, n*(n-1) is much larger than n*(n-1)/2, so we can ignore the division and just return n*(n-1). This is why the answer is n*(n-1).  # noqa: E501


