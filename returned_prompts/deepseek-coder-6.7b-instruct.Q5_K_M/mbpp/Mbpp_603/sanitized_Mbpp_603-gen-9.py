def get_ludic(n):
    ludic_numbers = []
    for i in range(1, n+1):
        if i & (i-1) == 0:
            ludic_numbers.append(i)
    return ludic_numbers