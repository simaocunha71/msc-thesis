def catalan_number(n: int) -> int:
    if n == 0:
        return 1
    if n == 1:
        return 1
    return (2*(n-1)**2)*catalan_number(n-2)+(n-1)**2