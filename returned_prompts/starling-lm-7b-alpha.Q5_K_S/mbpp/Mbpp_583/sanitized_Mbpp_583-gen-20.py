def catalan_number(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return catalan_number(n-1) + catalan_number(n-2) * (2*n-1)