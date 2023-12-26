

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if not (0 < n <= 10): return -9999
    # Find factors of n:
    t = []
    for i in range(n // 2, int(sqrt(n)) + 1, 2):
        t += [i]
    r = sorted(t)[-1]
    
    return r if (r < n) else largest_divisor(int((r - 1) / 2))
        