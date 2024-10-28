def bell_number(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return sum(bell_number(i) for i in range(n)) if n > 1 else 1