    return sum(val**2 if i%3==0 else (val**3 if i%4==0 else val) for i, val in enumerate(lst))


