    return sum(i ** 2 for i in (x for x in lst if isinstance(x, int) and x % 2 != 0)) if lst else 0


