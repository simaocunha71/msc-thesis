    if n == 1:
        return [1]
    elif n % 2 == 0:
        return get_odd_collatz(n // 2)
    else:
        return get_odd_collatz(n * 3 + 1) + [n] if n != 1 else [1]

