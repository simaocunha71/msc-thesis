    if not lst:
        return 0

    return sum(x ** 2 for x in lst if x % 2)


