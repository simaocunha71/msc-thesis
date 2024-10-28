def bell_Number(n):
    """
    The nth bell number is the number of ways to split n identical balls into n groups in such a way that no group contains more than one ball.
    """
    if n == 1:
        return 1
    return sum(bell_Number(i) * bell_Number(n-i-1) for i in range(n))


