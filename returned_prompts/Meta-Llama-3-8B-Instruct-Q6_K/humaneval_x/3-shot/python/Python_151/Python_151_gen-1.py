    return sum(i**2 for i in lst if isinstance(i, int) and i % 2 != 0) if lst else 0


