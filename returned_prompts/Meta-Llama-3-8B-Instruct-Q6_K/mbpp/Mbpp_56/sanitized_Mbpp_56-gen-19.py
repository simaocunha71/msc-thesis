def check(n):
    if not isinstance(n, int) or n < 0:
        return False  # or raise an error
    reverse = int(str(n)[::-1])
    return n == 2 * reverse - 1