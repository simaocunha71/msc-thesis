def is_polite(n):
    """Check if a number is polite."""
    count = 0
    i = 1
    while i * (i + 1) // 2 < n:
        count += 1
        i += 1
    return n == i * (i + 1) // 2 + count