
def is_woodall(n):
    return all(n % i for i in range(2, n))


