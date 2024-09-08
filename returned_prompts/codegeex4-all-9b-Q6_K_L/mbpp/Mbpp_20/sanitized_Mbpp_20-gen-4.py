def is_woodall(n):
    """
    A Woodall number is a number of the form w(n) = n * 2^n - 1 for some integer n.
    """
    def woodall(n):
        return n * (2 ** n) - 1

    return n == woodall(n)