def bell_number(n):
    if n == 0 or n == 1:
        return 1
    return sum(bell_number(i) for i in range(n))