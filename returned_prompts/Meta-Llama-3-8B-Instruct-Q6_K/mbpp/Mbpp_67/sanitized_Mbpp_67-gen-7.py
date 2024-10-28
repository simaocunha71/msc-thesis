def bell_number(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return sum(bell_number(i) for i in range(1, n+1))